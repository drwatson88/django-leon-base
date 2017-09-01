# coding: utf-8


from django.db import models


class SocialLinksMenuItem(models.Model):

    name = models.CharField(verbose_name='Обозначение пункта меню', max_length=255)
    position = models.IntegerField(verbose_name='Позиция пункта',
                                   help_text='Позиция слева направо в шапке сайта')

    class Meta:
        abstract = True
        verbose_name = 'Пункт меню шапки сайта'
        verbose_name_plural = 'Пункты меню шапки сайта'

    def __str__(self):
        return self.name

