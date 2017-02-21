# coding: utf-8


from leon.base import BaseContextProcessor
from .converters import HeaderConverterMixin


class HeaderContextProcessor(BaseContextProcessor, HeaderConverterMixin):
    """
    Class for header context processor menu
    """
    ADMIN_SETTINGS_MODEL = None
    HEADER_SETTINGS_MODEL = None

    def _create_data(self):
        self.header_settings = self.HEADER_SETTINGS_MODEL.objects.all()[0] \
            if self.HEADER_SETTINGS_MODEL.objects.all() else {}
        self.admin_settings = self.ADMIN_SETTINGS_MODEL.objects.all()[0] \
            if self.ADMIN_SETTINGS_MODEL.objects.all() else {}

    def __call__(self, request):
        self.header = {}
        self.output_context = {
            'header': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context


