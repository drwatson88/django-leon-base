# coding: utf-8


from django.db import models


class PrimaryMenuItem(models.Model):

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
