# -*- coding: utf-8 -*-


from django.utils.safestring import mark_safe
from django.contrib.sites.shortcuts import get_current_site
from leon.apps.site.base import FrontSiteBaseView, FrontSiteParamsValidatorMixin


class FrontFlatpagesView(FrontSiteBaseView, FrontSiteParamsValidatorMixin):

    """ Front Flatpage View. Receives get params
        and response neither arguments in get
        request params.

        GET Params.

        ALL PARAMS put in params_storage after validate
    """

    template_name = 'flatpages/default.html'
    FLATPAGE_MODEL = None

    kwargs_params_slots = {
        'url': [None, ''],
    }

    def __init__(self, *args, **kwargs):
        self.params_storage = {}
        self.output_context = {
            'flatpage': None
        }
        super(FrontFlatpagesView, self).__init__(*args, **kwargs)

    def _set_flatpage(self):
        site_id = get_current_site(self.request).id
        url = self.params_storage['url']
        if not url.startswith('/'):
            url = '/' + url
        flatpage = self.FLATPAGE_MODEL.objects.\
            filter(url=url, sites=site_id).first()
        if not flatpage:
            self.flatpage = {}
        self.flatpage = {
            'title': mark_safe(flatpage.title),
            'content': mark_safe(flatpage.content)
        }

    def get(self, *args, **kwargs):
        self._set_flatpage()
        self._aggregate()
        return self._render()
