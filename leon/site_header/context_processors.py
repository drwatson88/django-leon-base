# coding: utf-8


from leon.site_base import BaseContextProcessor
from .converters import ConverterMixin


class HeaderContextProcessor(BaseContextProcessor, ConverterMixin):
    """
    Class for header context processor menu
    """
    MENU_ITEM_MODEL = None
    SITE_SETTINGS_MODEL = None
    HEADER_MODEL = None

    def _create_data(self):
        self.menu_item_s = self.MENU_ITEM_MODEL.objects.all()
        self.header_settings = self.HEADER_MODEL.objects.all()[0] \
            if self.HEADER_MODEL.objects.all() else {}
        self.site_settings = self.SITE_SETTINGS_MODEL.objects.all()[0] \
            if self.SITE_SETTINGS_MODEL.objects.all() else {}

    def __call__(self, request):
        self.header = {}
        self.output_context = {
            'menu_header': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context


