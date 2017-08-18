# coding: utf-8


from leon.base import BaseContextProcessor


class RightsContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    RIGHTS_MODEL = None

    def _create_data(self):
        self.rights_desc = self.RIGHTS_MODEL.objects.first()

    def _format(self):
        pass

    def __call__(self, request):
        self.rights_desc = {}
        self.output_context = {
            'rights_desc': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context
