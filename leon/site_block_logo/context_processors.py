# coding: utf-8


from leon.base import BaseContextProcessor


class LogoContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    LOGO_MENU_MODEL = None

    def _create_data(self):
        self.logo = self.LOGO_MODEL.objects.first()

    def _format(self):
        pass

    def __call__(self, request):
        self.logo = {}
        self.output_context = {
            'logo': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context
