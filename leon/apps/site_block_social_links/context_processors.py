# coding: utf-8


from leon.base import BaseContextProcessor


class SocialLinksContextProcessor(BaseContextProcessor):
    """
    Class for social links context processor menu
    """
    SOCIAL_LINK_MODEL = None

    def _create_data(self):
        self.social_link_s = self.SOCIAL_LINK_MODEL.objects.all().order_by('position')

    def __call__(self, request):
        self.header = {}
        self.output_context = {
            'social_link_s': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context
