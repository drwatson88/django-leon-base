# coding: utf-8


from leon.base import BaseContextProcessor


class MainMenuContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    MAIN_MENU_ITEM_MODEL = None

    def _create_data(self):
        self.main_menu = self.MAIN_MENU_ITEM_MODEL.objects.all().order_by('position')

    def _format(self):
        pass

    def __call__(self, request):
        self.main_menu = {}
        self.output_context = {
            'main_menu': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context


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


