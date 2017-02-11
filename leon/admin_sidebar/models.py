# coding: utf-8


import os
import hashlib
from pytils.translit import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from django.db import models
from treebeard.mp_tree import MP_Node


class SidebarSettings(models.Model):

    def logo_upload_path(self, instance):
        return os.path.join('upload_header', '{}{}'.
                            format(hashlib.md5(slugify(instance).
                                               encode(encoding='utf-8')).hexdigest(), '.jpg'))

    logo = models.ImageField(verbose_name='Логотип',
                             blank=True, max_length=255,
                             upload_to=logo_upload_path)
    phone = models.CharField(verbose_name='Телефон', max_length=20)

    class Meta:
        abstract = True
        verbose_name = 'Настройки шапки сайта'
        verbose_name_plural = 'Настройки шапки сайта'

    def __str__(self):
        return 'Настройки шапки сайта'


class SidebarLinkItem(MP_Node):

    title = models.CharField(verbose_name='Название пункта меню', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)

    class Meta:
        abstract = True
        verbose_name = 'Пункт дерева ссылок'
        verbose_name_plural = 'Пункты дерева ссылок'

    class Options:
        native = True

    def __str__(self):
        return '{}{}'.format((self.depth - 1) * '---', self.slug_title)


class SidebarMenuItem(models.Model):

    name = models.CharField(verbose_name='Обозначение пункта меню', max_length=255)
    position = models.IntegerField(verbose_name='Позиция пункта',
                                   help_text='Позиция слева направо в шапке сайта')
    item_content_type = models.ForeignKey(ContentType)
    item_object_id = models.PositiveIntegerField()
    item_content_object = GenericForeignKey('item_content_type', 'item_object_id')

    class Meta:
        abstract = True
        verbose_name = 'Пункт меню шапки сайта'
        verbose_name_plural = 'Пункты меню шапки сайта'

    def __str__(self):
        return self.name
