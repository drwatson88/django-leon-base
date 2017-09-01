# coding: utf-8


from django.db import models


class SmallDescMenuItem(models.Model):

    title = models.CharField(verbose_name='Название краткого описания', max_length=255)
    show = models.BooleanField(verbose_name='Показывать', default=True)
    desc = models.TextField(verbose_name='Краткое описание')

    class Meta:
        abstract = True
        verbose_name = 'Краткое описание'
        verbose_name_plural = 'Краткое описание'

    def __str__(self):
        return self.title
