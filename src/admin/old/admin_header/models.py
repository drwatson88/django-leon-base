# coding: utf-8


import os
import hashlib
from django.db import models
from pytils.translit import slugify


class HeaderSettings(models.Model):

    def logo_upload_path(self, instance):
        return os.path.join('upload_header', '{}{}'.
                            format(hashlib.md5(slugify(instance).
                                               encode(encoding='utf-8')).hexdigest(), '.jpg'))

    logo = models.ImageField(verbose_name='Логотип',
                             blank=True, max_length=255,
                             upload_to=logo_upload_path)

    class Meta:
        abstract = True
        verbose_name = 'Настройки шапки админки'
        verbose_name_plural = 'Настройки шапки админки'

    def __str__(self):
        return 'Настройки шапки админки'
