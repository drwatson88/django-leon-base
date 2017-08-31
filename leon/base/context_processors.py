# coding: utf-8


class BaseContextProcessor(object):

    kwargs_params_slots = {}
    request_params_slots = {}
    session_params_slots = {}
    session_save_slots = {}
    params_storage = {}
    output_context = {}

    def _init(self, request):
        self._install_validate_s(request)
        self._validate(request)
        self.output_context = self.output_context or {}

    def _install_validate_s(self, request):
        for param in self.request_params_slots:
            self.request_params_slots[param][0] = \
                getattr(self, '_{param}_validator'.format(param=param))
        for param in self.session_params_slots:
            self.session_params_slots[param][0] = \
                getattr(self, '_{param}_validator'.format(param=param))
        for param in self.kwargs_params_slots:
            self.kwargs_params_slots[param][0] = \
                getattr(self, '_{param}_validator'.format(param=param))

    def _validate(self, request):

        """ Determine for every param

            :param request Request http
            :type request object

        """

        self.params_storage = {}
        session = getattr(request, 'session')
        method_params = getattr(request, getattr(request, 'method').upper())
        kwargs_params = getattr(request, 'kwargs_params')

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

        kwargs_validators = getattr(self, 'kwargs_params_slots')
        for k, v in kwargs_validators.items():
            validator = v[0]
            default = v[1]
            self.params_storage[k] = validator(kwargs_params.get(k), default)

    def _aggregate(self):
        for item in self.output_context:
            self.output_context[item] = getattr(self, item, self.output_context[item])

    def _format(self):
        pass