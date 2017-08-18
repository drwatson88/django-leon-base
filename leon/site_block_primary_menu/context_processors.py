# coding: utf-8


from leon.base import BaseContextProcessor


class PrimaryMenuContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    PRIMARY_MENU_ITEM_MODEL = None

    def _create_data(self):
        self.primary_menu = self.PRIMARY_MENU_ITEM_MODEL.objects.all().order_by('position')

    def _format(self):
        pass

    def __call__(self, request):
        self.primary_menu = {}
        self.output_context = {
            'primary_menu': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context
