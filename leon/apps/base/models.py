# coding: utf-8


import os
import hashlib
from django.utils.text import slugify
from django.db import models


class BaseUidMixin(models.Model):

    """ Show Mixin
    """

    uid = models.CharField(verbose_name='UID', null=False, blank=False, max_length=10, unique=True)

    class Meta:
        abstract = True


class BaseStatusMixin(models.Model):

    """ Show Mixin
    """

    STATUSES = [
        (0, 'Активен'),
        (1, '1'),
        (2, '2'),
        (3, '3')
    ]

    status = models.IntegerField(verbose_name='Статус', choices=STATUSES, default=0)

    class Meta:
        abstract = True


class BaseShowMixin(models.Model):

    """ Show Mixin
    """

    show = models.BooleanField(verbose_name='Показывать', default=True)

    class Meta:
        abstract = True


class BasePositionMixin(models.Model):

    """ Position Mixin
    """

    position = models.IntegerField(verbose_name='Позиция', blank=True, null=True)

    class Meta:
        abstract = True


class BaseSeoMixin(models.Model):

    """ Main Seo fields Mixin
    """

    content_seo = models.TextField(verbose_name='Описание для SEO', blank=True, null=True)
    title_seo = models.CharField(verbose_name='Заголовок для SEO', max_length=255, blank=True,
                                 null=True)
    meta_key = models.CharField(verbose_name='Meta key', max_length=255, blank=True,
                                null=True)
    meta_des = models.CharField(verbose_name='Meta des', max_length=255, blank=True,
                                null=True)

    class Meta:
        abstract = True


class BaseImageUploadMixin(models.Model):

    """ Image Upload Mixin - use upload_directory
        for set DIR, where save images
    """

    upload_image_directory = ''

    def image_upload_path(self, instance):
        return os.path.join(self.upload_image_directory,
                            '{}{}{}{}'.format(self.article.pk, self.meaning, self.position, '.jpg'))

    image = models.ImageField(verbose_name='Путь к файлу картинки',
                              blank=True, max_length=255,
                              upload_to=image_upload_path)

    class Meta:
        abstract = True


class BaseFileUploadMixin(models.Model):

    """ File Upload Mixin - use upload_directory
        for set DIR, where save files
    """

    upload_file_directory = ''

    def file_upload_path(self, instance):
        return os.path.join(self.upload_file_directory,
                            '{}{}{}{}'.format(self.article.pk, self.meaning, self.position, '.jpg'))

    file = models.FileField(verbose_name='URL доп.файла',
                            upload_to=file_upload_path,
                            blank=True)

    class Meta:
        abstract = True


class BaseExtraJsonModel(models.Model):

    """ Extra Json Model
    """

    extra_field = models.CharField(verbose_name='Доп. объекты', max_length=10000,
                                   blank=True, null=True)

    def __str__(self):
        return self.parent.title

    class Meta:
        abstract = True



