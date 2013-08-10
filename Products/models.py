# coding=utf-8
from django.db import models


class Manufacturers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', blank=False, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'manufacturers'


class Genre():
    name = models.CharField(max_length=100, verbose_name='Название', blank=False, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'manufacturers'


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(decimal_places=2, max_digits=99999, verbose_name='Цена', null=True)
    count = models.IntegerField(verbose_name='Количество', default=0)
    full_description = models.TextField(verbose_name='Описание')
    brief_description = models.TextField(verbose_name='Краткое описание')
    active = models.BooleanField(verbose_name='Активен', default=False)
    manufacturer = models.ForeignKey(Manufacturers)

    class Meta:
        db_table = 'products'

    def __unicode__(self):
        return u'{}:{}'.format(self.manufacturer, self.name)
        #manufacturer =