# -*- coding: utf-8 -*-

from functools import update_wrapper
import re

from django.views.generic import View
from django.utils.decorators import classonlymethod
from django.template import RequestContext
from django.shortcuts import render


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

    def __init__(self, **kwargs):
        self.params_storage = self.params_storage or {}
        self.output_context = self.output_context or {}
        super(BaseView, self).__init__(**kwargs)

    def _format(self):
        pass

    def _aggregate(self):
        for item in self.output_context:
            self.output_context[item] = getattr(self, item, self.output_context[item])

    def _save_cookies(self):
        for item in self.session_save_slots:
            if item not in self.request.session:
                self.request.session[item] = getattr(self, self.session_save_slots[item])

    @staticmethod
    def _exclude_assets(html):
        css_storage = set()
        js_storage = set()

        def replace_css(obj):
            if obj.group(0) in css_storage:
                return ''
            else:
                css_storage.add(obj.group(0))
                return obj.group(0)

        def replace_js(obj):
            if obj.group(0) in js_storage:
                return ''
            else:
                js_storage.add(obj.group(0))
                return obj.group(0)

        css_pattern = re.compile(r'(@import "/static/.+\.css";)')
        js_pattern = re.compile(r'(<script src="/static/.+\.js"></script>)')
        html = re.sub(css_pattern,
                      replace_css,
                      html)
        html = re.sub(js_pattern,
                      replace_js,
                      html)
        return html

    def _render(self):
        response = render(
            self.request,
            self._get_template_name(),
            self.output_context)
        render_html = self._exclude_assets(response.content.decode('utf-8'))
        response.content = render_html.encode('utf-8')
        return response

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

        session_validators = getattr(self, 'cookies_params_slots')
        for k, v in session_validators.items():
            validator = v[0]
            default = v[1]
            self.params_storage[k] = validator(session.get(k), default)

        kwargs_validators = getattr(self, 'kwargs_params_slots')
        for k, v in kwargs_validators.items():
            validator = v[0]
            default = v[1]
            self.params_storage[k] = validator(kwargs.get(k), default)

        return super(BaseView, self).dispatch(request, *args, **kwargs)
