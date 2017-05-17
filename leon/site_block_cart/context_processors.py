# coding: utf-8


from leon.base import BaseContextProcessor
from .converters import MainMenuConverterMixin


class MainMenuContextProcessor(BaseContextProcessor, MainMenuConverterMixin):
    """
    Class for header context processor menu
    """
    HEADER_MENU_ITEM_MODEL = None
    SITE_SETTINGS_MODEL = None
    HEADER_SETTINGS_MODEL = None

    def _create_data(self):
        self.menu_item_s = self.HEADER_MENU_ITEM_MODEL.objects.all().order_by('position')
        self.header_settings = self.HEADER_SETTINGS_MODEL.objects.first()
        self.site_settings = self.SITE_SETTINGS_MODEL.objects.first()

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


