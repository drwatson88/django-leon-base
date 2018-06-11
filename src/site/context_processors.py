# coding: utf-8


from ..base.context_processors import BaseContextProcessor


class FrontMainMenuContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    MAIN_MENU_ITEM_MODEL = None

    def _create_data(self):
        self.main_menu = self.MAIN_MENU_ITEM_MODEL.objects.filter(show=True).order_by('position')

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


class FrontSidebarMenuContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    SIDEBAR_MENU_ITEM_MODEL = None

    def _create_data(self):
        self.sidebar_menu = self.SIDEBAR_MENU_ITEM_MODEL.objects.all().order_by('position')

    def _format(self):
        pass

    def __call__(self, request):
        self.sidebar_menu = {}
        self.output_context = {
            'sidebar_menu': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context


class FrontAdditionalLinkContextProcessor(BaseContextProcessor):
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


class FrontLogoHeaderContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    LOGO_HEADER_MODEL = None

    def _create_data(self):
        self.logo_header = self.LOGO_HEADER_MODEL.objects.first()

    def _format(self):
        pass

    def __call__(self, request):
        self.logo = {}
        self.output_context = {
            'logo_header': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context


class FrontLogoFooterContextProcessor(BaseContextProcessor):
    """
    Class for block context processor menu
    """
    LOGO_FOOTER_MODEL = None

    def _create_data(self):
        self.logo_footer = self.LOGO_FOOTER_MODEL.objects.first()

    def _format(self):
        pass

    def __call__(self, request):
        self.logo = {}
        self.output_context = {
            'logo_footer': None
        }
        self._init(request)
        self._create_data()
        self._format()
        self._aggregate()
        return self.output_context


class FrontPhotoStreamContextProcessor(BaseContextProcessor):
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


class FrontPrimaryMenuContextProcessor(BaseContextProcessor):
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


class FrontRightsDescContextProcessor(BaseContextProcessor):
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


class FrontSmallDescContextProcessor(BaseContextProcessor):
    """
    Class for block context processor
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


class FrontSocialLinksContextProcessor(BaseContextProcessor):
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
        self._aggregate()
        return self.output_context


class FrontUserCityContextProcessor(BaseContextProcessor):
    """
    Class for user city context processor menu
    """
    USER_CITY_MODEL = None

    def _create_data(self):
        self.user_city_s = self.USER_CITY_MODEL.objects.filter(is_main=True).all().order_by('name')

    def _current_city(self):
        session = self.request.session
        self.user_city_selected = session.get('city_id')

    def __call__(self, request):
        self.header = {}
        self.output_context = {
            'user_city_s': None,
            'user_city_selected': None
        }
        self._init(request)
        self._create_data()
        self._current_city()
        self._aggregate()
        return self.output_context


class FrontWorkingDescContextProcessor(BaseContextProcessor):
    """
    Class for working desc
    """
    WORKING_DESC_MODEL = None

    def _create_data(self):
        self.working_desc = self.WORKING_DESC_MODEL.objects.first()

    def __call__(self, request):
        self.header = {}
        self.output_context = {
            'working_desc': None
        }
        self._init(request)
        self._create_data()
        self._aggregate()
        return self.output_context
