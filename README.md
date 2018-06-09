# About project

This library created from me for using in bulding some sites with Django framework. Library has more effectively wrappers for smart using Django.


## Getting Started (Examples)
~~~
Creating Model for CallBack with Mixins:

from leon_base.base.models import BaseUidMixin, BaseStatusMixin
from leon_base.site.models import BaseCallBackItem
class CallBackItem(BaseCallBackItem, BaseUidMixin, BaseStatusMixin):
    pass

Creating View for Messages List:

from leon_base.site.views import FrontCallBackView
class CallBackView(FrontCallBackView):
    CALLBACK_MODEL = CallBackItem
    EMAIL_CALLBACK_SUBJECT = 'e-mail test subject'
    EMAIL_CALLBACK_MESSAGE = 'e-mail test message'
~~~ 

### Prerequisites

Python >= 3.5
Django >= 1.11


### Installing
~~~
pip install git+http://github.com/dvsidorov/django-leon-base.git
~~~

### Building documentation
~~~
git clone http://github.com/dvsidorov/django-leon-base.git djleon_base
cd ./djleon_base/docs/
make html
~~~

## Built With

* [Django](https://github.com/django/django.git) - The web framework used


## Authors

* **Denis Sidorov** - *Initial work* - [dvsidorov](https://github.com/dvsidorov)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
