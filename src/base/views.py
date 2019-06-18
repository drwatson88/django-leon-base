# -*- coding: utf-8 -*-


from django.conf import settings
from django.utils.module_loading import import_string
from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.loader import render_to_string


class BaseParamsValidatorMixin(object):

    """ Mixin with validators for validate
        request parameters.
    """

    pass


class BaseView(View):

    """ Class Base for all Catalog Class Views
        When request is received, then
    """

    kwargs_params_slots = {}
    request_params_slots = {}
    session_params_slots = {}
    cookies_params_slots = {}
    session_save_slots = {}
    params_storage = {}
    output_context = {}
    extra_context = {}

    template_name = None
    template_popup = None
    popup = None
    context_processors = []

    def __init__(self, **kwargs):
        self.params_storage = self.params_storage or {}
        self.output_context = self.output_context or {}
        super(BaseView, self).__init__(**kwargs)

    def _aggregate(self):
        for item in self.output_context:
            self.output_context[item] = getattr(self, item, self.output_context[item])

    def _save_cookies(self):
        for item in self.session_save_slots:
            if item not in self.request.session:
                self.request.session[item] = getattr(self, self.session_save_slots[item])

    def _context_processors(self):
        base_context_processors = settings.BASE_CONTEXT_PROCESSORS + self.context_processors
        context_processors = \
            set(import_string(item) for item in base_context_processors if isinstance(item, str)) | \
            set(item for item in base_context_processors if not isinstance(item, str))
        _context_processors = \
            set(item() for item in context_processors if isinstance(item, type)) | \
            set(item for item in context_processors if not isinstance(item, type))
        context = {}
        for cp in _context_processors or []:
            context.update(cp(self.request))
        self.output_context.update(context)

    def _render(self):
        if self.popup:
            return self._render_popup()
        else:
            return self._render_page()

    def _render_page(self):
        setattr(self.request, 'kwargs_params', self.kwargs)
        self._aggregate()
        self._context_processors()
        return render_to_response(self._get_template_name(),
                                  self.output_context)

    def _render_popup(self):
        setattr(self.request, 'kwargs_params', self.kwargs)
        self._aggregate()
        self._context_processors()
        response = {}
        for k, v in self.template_popup.items():
            response.update({k: render_to_string(v, self.output_context)})
        response.update(self.data_popup)
        return JsonResponse(response)

    def _get_template_name(self):
        return self.template_name

    @classmethod
    def _install_validate_s(cls):
        for param in cls.request_params_slots:
            cls.request_params_slots[param][0] = \
                getattr(cls, '_{param}_validator'.format(param=param))
        for param in cls.session_params_slots:
            cls.session_params_slots[param][0] = \
                getattr(cls, '_{param}_validator'.format(param=param))
        for param in cls.kwargs_params_slots:
            cls.kwargs_params_slots[param][0] = \
                getattr(cls, '_{param}_validator'.format(param=param))

    @classmethod
    def as_view(cls, **initkwargs):
        cls._install_validate_s()
        return super(BaseView, cls).as_view(**initkwargs)

    def dispatch(self, request, *args, **kwargs):

        """ Dispatch redetermine for route in validate
            for every method and every param

            :param request Request http
            :type request object

        """

        self.params_storage = {}
        method = getattr(request, 'method')
        session = getattr(request, 'session')
        cookies = getattr(request, 'COOKIES')
        method_params = getattr(request, method.upper())
        request_validators = getattr(self, 'request_params_slots')
        for k, v in request_validators.items():
            validator = v[0]
            default = v[1]
            self.params_storage[k] = validator(method_params.get(k), default)

        session_validators = getattr(self, 'session_params_slots')
        for k, v in session_validators.items():
            validator = v[0]
            default = v[1]
            self.params_storage[k] = validator(session.get(k), default)

        cookies_validators = getattr(self, 'cookies_params_slots')
        for k, v in cookies_validators.items():
            validator = v[0]
            default = v[1]
            self.params_storage[k] = validator(cookies.get(k), default)

        kwargs_validators = getattr(self, 'kwargs_params_slots')
        for k, v in kwargs_validators.items():
            validator = v[0]
            default = v[1]
            self.params_storage[k] = validator(kwargs.get(k), default)

        return super(BaseView, self).dispatch(request, *args, **kwargs)
