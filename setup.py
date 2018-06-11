#!/usr/bin/env python

from distutils.core import setup


setup(
    name='django-leon-base',
    version='0.1.1',
    description='Python Base Django Utils',
    author='Denis Sidorov',
    author_email='dvsidorov88@mail.ru',
    url='https://github.com/dvsidorov/django-leon-base',
    packages=['leon_base',
              'leon_base.auth',
              'leon_base.admin',
              'leon_base.base',
              'leon_base.settings',
              'leon_base.site'],
    package_dir={'leon_base': 'src'}
)
