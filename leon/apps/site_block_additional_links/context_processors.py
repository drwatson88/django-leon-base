# coding: utf-8


from leon.base import BaseContextProcessor


class AdditionalLinkContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    ADDITIONAL_LINK_ITEM_MODEL = None

    def _create_data(self):
        self.additional_link_s = self.ADDITIONAL_LINK_ITEM_MODEL.objects.all().order_by('position')

    def _format(self):
        pass

    def __call__(self, request):
        self.additional_link_s = {}
        self.output_context = {
            'additional_link_s': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context
