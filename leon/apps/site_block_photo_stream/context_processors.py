# coding: utf-8


from leon.base import BaseContextProcessor


class PhotoStreamContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    PHOTO_STREAM_MODEL = None

    def _create_data(self):
        self.photo_stream = self.PHOTO_STREAM_MODEL.objects.first()

    def _format(self):
        pass

    def __call__(self, request):
        self.photo_stream = {}
        self.output_context = {
            'photo_stream': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context
