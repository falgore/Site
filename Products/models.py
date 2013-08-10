# coding=utf-8
from django.db import models


class Manufacturers(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'manufacturers'


class Genres(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'genres'


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Название')
    price = models.DecimalField(decimal_places=2, max_digits=65, verbose_name=u'Цена', null=True)
    count = models.IntegerField(verbose_name=u'Количество', default=0)
    full_description = models.TextField(verbose_name=u'Описание')
    brief_description = models.TextField(verbose_name=u'Краткое описание')
    active = models.BooleanField(verbose_name=u'Активен', default=False)
    manufacturer = models.ForeignKey(Manufacturers)
    genre = models.ForeignKey(Genres)

    class Meta:
        db_table = u'products'

    def __unicode__(self):
        return u'{}:{}'.format(self.manufacturer, self.name)