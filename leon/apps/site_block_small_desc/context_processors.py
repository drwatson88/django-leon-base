# coding: utf-8


from leon.base import BaseContextProcessor


class SmallDescContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    SMALL_DESC_MODEL = None

    def _create_data(self):
        self.small_desc = self.SMALL_DESC_MODEL.objects.first()

    def _format(self):
        pass

    def __call__(self, request):
        self.small_desc = {}
        self.output_context = {
            'small_desc': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context
