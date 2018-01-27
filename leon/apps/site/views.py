# -*- coding: utf-8 -*-


from django.utils.safestring import mark_safe
from django.http import JsonResponse
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


class FrontCallBackView(FrontSiteBaseView, FrontSiteParamsValidatorMixin):

    """ Front CallBack View. Receives get params
        and response neither arguments in get
        request params.

        GET Params.

        ALL PARAMS put in params_storage after validate
    """

    CALLBACK_MODEL = None

    request_params_slots = {
        'phone': [None, '']
    }

    kwargs_params_slots = {
    }

    def __init__(self, *args, **kwargs):
        self.params_storage = {}
        self.output_context = {
            'success': None
        }
        super(FrontCallBackView, self).__init__(*args, **kwargs)

    def _phone_set(self):
        self.phone = self.params_storage['phone']

    def _phone_validate(self):
        pass

    def _phone_save(self):
        callback = self.CALLBACK_MODEL.objects.create(phone=self.phone)
        callback.save()

    def post(self, *args, **kwargs):
        self._phone_set()
        self._phone_validate()
        self._phone_save()
        self._aggregate()
        return JsonResponse({'success': True})
