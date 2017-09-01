# coding: utf-8


import os
import hashlib
from pytils.translit import slugify
from django.db import models


class LogoMenuItem(models.Model):

    def logo_upload_path(self, instance):
        return os.path.join('upload_settings', '{}{}'.
                            format(hashlib.md5(slugify(self.title).
                                               encode(encoding='utf-8')).hexdigest(), '.jpg'))

    title = models.CharField(verbose_name='Название пункта меню', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    src = models.ImageField(verbose_name='Путь к файлу изображения', upload_to=logo_upload_path)

    class Meta:
        abstract = True
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'

    def __str__(self):
        return self.title
