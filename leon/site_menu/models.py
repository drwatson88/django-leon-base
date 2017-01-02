# coding: utf-8


from django.db import models
from treebeard.mp_tree import MP_Node


class MenuItem(object):

    href = models.CharField('Ссылка', max_length=255, blank=True, null=True)
    name = models.CharField('Название', max_length=128, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = "Настройка пункта меню"
        verbose_name_plural = "Настройки пунктов меню"


class MenuItemCategory(MP_Node):

    title = models.CharField('Заголовок', max_length=255)
    preview = models.TextField('Краткое описание', blank=True, null=True)
    show = models.BooleanField('Показывать', default=True)
    image = models.ImageField('Изображение', blank=True, null=True)
    position = models.IntegerField('Позиция', blank=True, null=True)
    href = models.CharField('Ссылка', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Категория пунктов меню'
        verbose_name_plural = 'Категории пунктов меню'

    def __str__(self):
        return '{}{}'.format((self.depth - 1) * '---', self.slug_title)

