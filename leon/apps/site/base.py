# -*- coding: utf-8 -*-

import json
from leon.apps.base import BaseView, BaseParamsValidatorMixin


class FrontSiteParamsValidatorMixin(BaseParamsValidatorMixin):

    """ Mixin with validators for validate
        request parameters.
    """

    @staticmethod
    def _url_validator(value, default):
        return value

    @staticmethod
    def _phone_validator(value, default):
        return value


class FrontSiteBaseView(BaseView):

    """ Class Base for all Front Class Views
        When request is received, then
    """

    pass
