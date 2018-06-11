# -*- coding: utf-8 -*-


from ..base.views import BaseView, BaseParamsValidatorMixin


class CommonSecurityParamsValidatorMixin(BaseParamsValidatorMixin):

    """ Mixin with validators for validate
        request parameters.
    """

    @staticmethod
    def _type_validator(value, default):
        try:
            return int(value)
        except BaseException as exc:
            return default

    @staticmethod
    def _data_validator(value, default):
        try:
            return int(value)
        except BaseException as exc:
            return default


class CommonSecurityView(BaseView):

    """ Class Base for all Common Auth Class Views
        When request is received, then
    """

    pass
