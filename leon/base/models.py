# coding: utf-8


from django.db import models


class TitleModel(models.Model):

    show = models.BooleanField(verbose_name='Показывать', default=True)

    class Meta:
        abstract = True


class ShowModel(models.Model):

    show = models.BooleanField(verbose_name='Показывать', default=True)

    class Meta:
        abstract = True
