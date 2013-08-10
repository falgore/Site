# coding=utf-8
from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(decimal_places=2, max_digits=99999, verbose_name='Цена')
