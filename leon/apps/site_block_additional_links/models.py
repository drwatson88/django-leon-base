# coding: utf-8


from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from django.db import models
from treebeard.mp_tree import MP_Node

from leon.base.models import TitleModel, ShowModel


class AdditionalLinkNode(TitleModel, ShowModel, MP_Node):

    title = models.CharField(verbose_name='Название пункта доп.ссылок', max_length=255)
    link = models.CharField(verbose_name='Ссылка', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)

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


class AdditionalLinkItem(models.Model):

    name = models.CharField(verbose_name='Обозначение пункта меню', max_length=255)
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
        verbose_name = 'Пункт дополнительных ссылок сайта'
        verbose_name_plural = 'Пункты дополнительных ссылок сайта'

    def __str__(self):
        return self.name
