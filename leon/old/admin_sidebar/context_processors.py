# coding: utf-8


from leon.base import BaseContextProcessor
from .converters import SidebarConverterMixin


class SidebarContextProcessor(BaseContextProcessor, SidebarConverterMixin):
    """
    Class for sidebar context processor menu
    """
    SIDEBAR_MENU_ITEM_MODEL = None
    ADMIN_SETTINGS_MODEL = None
    SIDEBAR_SETTINGS_MODEL = None
    SECTIONS = [{'key': 'dashboard',
                 'name': 'Панель управления',
                 'fa_icon': 'fa-dashboard',
                 'children': []},
                {'key': 'useful_links',
                 'name': 'Полезные ссылки',
                 'fa_icon': 'fa-dashboard',
                 'children': []}]

    def _create_data(self):
        self.sidebar_item_s = self.SIDEBAR_MENU_ITEM_MODEL.objects.filter(
            type__in=[item['key'] for item in self.SECTIONS]).all().order_by('position')
        self.sidebar_settings = self.SIDEBAR_SETTINGS_MODEL.objects.all()[0] \
            if self.SIDEBAR_SETTINGS_MODEL.objects.all() else {}
        self.admin_settings = self.ADMIN_SETTINGS_MODEL.objects.all()[0] \
            if self.ADMIN_SETTINGS_MODEL.objects.all() else {}

    def __call__(self, request):
        self.menu_sidebar = {}
        self.output_context = {
            'menu_sidebar': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context


