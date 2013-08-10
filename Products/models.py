# coding=utf-8
from django.db import models


class Manufacturers(models.Model):
    pass


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(decimal_places=2, max_digits=99999, verbose_name='Цена')
    count = models.IntegerField(verbose_name='Количество')
    full_description = models.TextField(verbose_name='Описание')
    brief_description = models.TextField(verbose_name='Краткое описание')
    active = models.BooleanField(verbose_name='Активен')
    #manufacturer =