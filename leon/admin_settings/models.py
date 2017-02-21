# coding: utf-8


from django.db import models


class Settings(models.Model):

    title = models.CharField(verbose_name='Название компании', help_text="под верхний логотип",
                             max_length=128, blank=True, null=True)
    slogan = models.CharField(verbose_name='Слоган', help_text="в шапку сайта над логотипом",
                              max_length=128, blank=True, null=True)
    logo = models.ImageField(verbose_name='Логотип', upload_to='upload_logo', blank=True, null=True)
    email = models.EmailField(verbose_name='E-mail', help_text="для отправки заказов и сообщений",
                              max_length=128, blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон подвала', max_length=1024, blank=True, null=True)
    copyright = models.CharField(verbose_name='Строка копирайта в подвале', max_length=1024,
                                 help_text='Все права защищены. Даты.', blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = 'Общие настройки админки'
        verbose_name_plural = 'Общие настройки админки'

    def __str__(self):
        return self.title
