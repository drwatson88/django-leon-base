# -*- coding: utf-8 -*-


from .base import CommonSecurityView, CommonSecurityParamsValidatorMixin


class CommonSecurityListView(CommonSecurityView, CommonSecurityParamsValidatorMixin):

    """ Common Auth View. Receives get params
        and response neither arguments in get
        request params.

        GET Params:

        1. AJAX - if ajax is True, we have response
        html part, that insert in DOM structure in client
        side. If we have True, we response all html
        document with base template.

        ALL PARAMS put in params_storage after validate
    """

    USER_MODEL = None

    request_params_slots = {
        'type': [None, 'login'],
        'data': [None, {}]
    }

    def __init__(self, *args, **kwargs):
        self.params_storage = {}
        self.output_context = {
        }
        super(CommonSecurityListView, self).__init__(*args, **kwargs)

    def _set_type(self):
        self.type = self.params_storage['type']

    def _authorization(self):
        if self.type != 'auth':
            return

    def _register(self):
        if self.type != 'register':
            return

    def get(self, *args, **kwargs):
        self._set_type()
        self._authorization()
        self._register()
        return self._render()

