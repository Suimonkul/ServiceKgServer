# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=50, unique=False, null=False)

    def __unicode__(self):
        return '%s' % (self.name)


class Advertisement(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=1000, unique=False, null=False)
    description = models.CharField(verbose_name='Описание', max_length=10000, unique=False, null=False)
    phone = models.IntegerField(verbose_name='Телефон', null=False)
    phone_two = models.IntegerField(verbose_name="Телефон 2", null=True, blank=True)
    phone_three = models.IntegerField(verbose_name="Телефон 3", null=True, blank=True)
    order = models.CharField(verbose_name="Цена услуги", blank=True, null=True, max_length=100)
    position = models.IntegerField(verbose_name='Позиция', null=False)
    category = models.ForeignKey(Category, null=True, verbose_name="Выберите категорию")

    # from_datetime = models.DateTimeField(null=True, verbose_name="FROM TIME")
    # to_datetime = models.DateTimeField(null=True, verbose_name="TO TIME")

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True, null=True)

    def __unicode__(self):
        return 'Категория = %s,  Позиция = %s,  Имя = %s ' % (self.category, self.position, self.name)


class PageDataAddition(object):
    def alter_list_data_to_serialize(self, request, data):
        data['category'] = {'title': True,
                            'names': 'sss',
                            'url': 'http://192.168.0.102/api/v1/advert/?format=json',
                            'int': 124,
                            'array': ['Комп', 'Мас', 'кас', 'стар']}
        return data
