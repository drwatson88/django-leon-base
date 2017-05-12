# coding: utf-8


from leon.base import BaseContextProcessor
from .converters import ConverterMixin


class FooterContextProcessor(BaseContextProcessor, ConverterMixin):
    """
    Class for footer context processor menu
    """
    FOOTER_MENU_ITEM_MODEL = None
    SITE_SETTINGS_MODEL = None
    FOOTER_SETTINGS_MODEL = None

    def _create_data(self):
        self.menu_item_s = self.FOOTER_MENU_ITEM_MODEL.objects.all()
        self.footer_settings = self.FOOTER_SETTINGS_MODEL.objects.all().first() \
            if self.FOOTER_SETTINGS_MODEL.objects.all() else {}
        self.site_settings = self.SITE_SETTINGS_MODEL.objects.all().first() \
            if self.SITE_SETTINGS_MODEL.objects.all() else {}

    def __call__(self, request):
        self.footer = {}
        self.output_context = {
            'footer': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context


