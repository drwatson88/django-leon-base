# coding: utf-8


import os
import hashlib
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from treebeard.mp_tree import MP_Node
from leon.apps.base.models import BaseShowMixin


class BaseMainMenuNode(BaseShowMixin, MP_Node):

    title = models.CharField(verbose_name='Название пункта меню', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    position = models.IntegerField(verbose_name='Позиция', blank=True, null=True)

    def get_show_children(self):
        return self.get_children().filter(show=True)

    def get_absolute_url(self):
        return self.link

    class Meta:
        abstract = True
        verbose_name = 'Пункт дерева ссылок меню'
        verbose_name_plural = 'Пункты дерева ссылок меню'

    def __str__(self):
        return '{}{}'.format((self.depth - 1) * '---', self.title)


class BaseMainMenuItem(models.Model):

    name = models.CharField(verbose_name='Обозначение пункта меню', max_length=255)
    title = models.CharField(verbose_name='Название пункта меню', max_length=255)
    position = models.IntegerField(verbose_name='Позиция пункта',
                                   help_text='Позиция слева направо в шапке сайта')
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    item_content_type = models.ForeignKey(ContentType, null=True, blank=True)
    item_object_id = models.PositiveIntegerField(null=True, blank=True)
    item_content_object = GenericForeignKey('item_content_type', 'item_object_id')

    @property
    def item(self):
        return self.item_content_object

    @item.setter
    def item(self, obj):
        self.item_content_object = obj

    def get_absolute_url(self):
        return self.link

    class Meta:
        abstract = True
        verbose_name = 'Пункт главного меню сайта'
        verbose_name_plural = 'Пункты главного меню сайта'

    def __str__(self):
        return self.name


class BaseAdditionalLinkNode(BaseShowMixin, MP_Node):

    title = models.CharField(verbose_name='Название пункта доп.ссылок', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    position = models.IntegerField(verbose_name='Позиция', blank=True, null=True)

    def get_show_children(self):
        return self.get_children().filter(show=True)

    @property
    def get_absolute_url(self):
        return self.link

    class Meta:
        abstract = True
        verbose_name = 'Пункт дерева ссылок доп.ссылок'
        verbose_name_plural = 'Пункты дерева ссылок доп.ссылок'

    def __str__(self):
        return '{}{}'.format((self.depth - 1) * '---', self.title)


class BaseAdditionalLinkItem(models.Model):

    name = models.CharField(verbose_name='Обозначение пункта доп.ссылок', max_length=255)
    title = models.CharField(verbose_name='Название пункта доп.ссылок', max_length=255)
    position = models.IntegerField(verbose_name='Позиция пункта',
                                   help_text='Позиция слева направо')
    item_content_type = models.ForeignKey(ContentType)
    item_object_id = models.PositiveIntegerField()
    item_content_object = GenericForeignKey('item_content_type', 'item_object_id')

    @property
    def item(self):
        return self.item_content_object

    @item.setter
    def item(self, obj):
        self.item_content_object = obj

    class Meta:
        abstract = True
        verbose_name = 'Пункт доп. ссылок сайта'
        verbose_name_plural = 'Пункты доп. ссылок сайта'

    def __str__(self):
        return self.name


class BaseLogoHeaderItem(models.Model):

    def logo_upload_path(self, instance):
        return os.path.join('upload_settings',
                            '{}{}'.format(hashlib.md5(slugify(self.title).
                                                      encode(encoding='utf-8')).hexdigest(), '.jpg'))

    title = models.CharField(verbose_name='Название пункта меню', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    src = models.ImageField(verbose_name='Путь к файлу изображения', upload_to=logo_upload_path)

    class Meta:
        abstract = True
        verbose_name = 'Логотип хедера'
        verbose_name_plural = 'Логотипы хедера'

    def __str__(self):
        return self.title


class BaseLogoFooterItem(models.Model):

    def logo_upload_path(self, instance):
        return os.path.join('upload_settings',
                            '{}{}'.format(hashlib.md5(slugify(self.title).
                                                      encode(encoding='utf-8')).hexdigest(), '.jpg'))

    title = models.CharField(verbose_name='Название пункта меню', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    src = models.ImageField(verbose_name='Путь к файлу изображения', upload_to=logo_upload_path)

    class Meta:
        abstract = True
        verbose_name = 'Логотип футера'
        verbose_name_plural = 'Логотипы футера'

    def __str__(self):
        return self.title


class BasePhotoStreamItem(models.Model):

    def photo_upload_path(self, instance):
        return os.path.join('upload_settings', '{}{}'.
                            format(hashlib.md5(slugify(self.title).
                                               encode(encoding='utf-8')).hexdigest(), '.jpg'))

    title = models.CharField(verbose_name='Название пункта фото', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    src = models.ImageField(verbose_name='Путь к файлу изображения', upload_to=photo_upload_path)

    class Meta:
        abstract = True
        verbose_name = 'Доска фото'
        verbose_name_plural = 'Доски фото'

    def __str__(self):
        return self.title


class BasePrimaryMenuItem(models.Model):

    title = models.CharField(verbose_name='Название пункта меню', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    position = models.IntegerField(verbose_name='Позиция пункта',
                                   help_text='Позиция слева направо в шапке сайта')

    class Meta:
        abstract = True
        verbose_name = 'Пункт верхнего меню сайта'
        verbose_name_plural = 'Пункты верхнего меню сайта'

    def __str__(self):
        return self.title


class BaseRightsDescItem(models.Model):

    title = models.CharField(verbose_name='Название', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    text = models.CharField(verbose_name='Текст', max_length=150)

    class Meta:
        abstract = True
        verbose_name = 'Права (информационное сообщение)'
        verbose_name_plural = 'Права (информационное сообщение)'

    def __str__(self):
        return self.title


class BaseSmallDescItem(models.Model):

    title = models.CharField(verbose_name='Название краткого описания', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    desc = models.TextField(verbose_name='Краткое описание')

    class Meta:
        abstract = True
        verbose_name = 'Краткое описание'
        verbose_name_plural = 'Краткое описание'

    def __str__(self):
        return self.title


class BaseSocialLinksItem(models.Model):

    name = models.CharField(verbose_name='Обозначение пункта', max_length=255)
    li_class = models.CharField(verbose_name='Класс li', max_length=20)
    fa_class_pfx = models.CharField(verbose_name='Префикс класса fa', max_length=20)
    position = models.IntegerField(verbose_name='Позиция пункта',
                                   help_text='Позиция слева направо в шапке сайта')

    class Meta:
        abstract = True
        verbose_name = 'Ссылка в соц.сети'
        verbose_name_plural = 'Ссылки в соц.сетях'

    def __str__(self):
        return self.name


class BaseWorkingDescItem(models.Model):

    name = models.CharField(verbose_name='Обозначение пункта', max_length=255)
    desc = models.TextField(verbose_name='Описание')
    m_fr = models.CharField(verbose_name='Пнд-Пт', max_length=30)
    saturday = models.CharField(verbose_name='Субб', max_length=30)
    sunday = models.CharField(verbose_name='Вскр', max_length=30)

    class Meta:
        abstract = True
        verbose_name = 'Краткое описание работы'
        verbose_name_plural = 'Краткие описания работы'

    def __str__(self):
        return self.name
