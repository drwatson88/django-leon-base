# coding: utf-8


from django.db import models
from treebeard.mp_tree import MP_Node


class Settings(models.Model):

    title = models.CharField('Название компании', help_text="под верхний логотип",
                             max_length=128, blank=True, null=True)
    slogan = models.CharField('Слоган', help_text="в шапку сайта над логотипом",
                              max_length=128, blank=True, null=True)
    logo = models.ImageField('Логотип', upload_to='upload_logo', blank=True, null=True)
    email = models.EmailField('E-mail', help_text="для отправки заказов и сообщений",
                              max_length=128, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=1024, blank=True, null=True)
    copyright = models.CharField('Строка копирайта в футере', max_length=1024,
                                 help_text="в футер", blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"


class Address(object):

    city = models.CharField('Название города', max_length=128, blank=True, null=True)
    street = models.CharField('Название улицы', max_length=128, blank=True, null=True)
    street_prefix = models.CharField('Префикс улицы', max_length=128, blank=True, null=True)
    house = models.CharField('Дом', max_length=128, blank=True, null=True)
    house_liter = models.CharField('Литера дома', max_length=128, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = "Настройка адреса"
        verbose_name_plural = "Настройки адреса"


class Link(object):

    href = models.CharField('Ссылка', max_length=255, blank=True, null=True)
    name = models.CharField('Название', max_length=128, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = "Настройка ссылки"
        verbose_name_plural = "Настройки ссылок"


class LinkCategory(MP_Node):

    title = models.CharField('Заголовок', max_length=255)
    preview = models.TextField('Краткое описание', blank=True, null=True)
    show = models.BooleanField('Показывать', default=True)
    image = models.ImageField('Изображение', blank=True, null=True)
    position = models.IntegerField('Позиция', blank=True, null=True)
    href = models.CharField('Ссылка', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Категория ссылок'
        verbose_name_plural = 'Категории ссылок'

    def __str__(self):
        return '{}{}'.format((self.depth - 1) * '---', self.slug_title)



