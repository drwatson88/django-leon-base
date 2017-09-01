# coding: utf-8


from django.db import models


class RightsItem(models.Model):

    title = models.CharField(verbose_name='Название', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    text = models.CharField(verbose_name='Текст')

    class Meta:
        abstract = True
        verbose_name = 'Права (информационное сообщение)'
        verbose_name_plural = 'Права (информационное сообщение)'

    def __str__(self):
        return self.title
