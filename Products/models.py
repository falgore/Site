# coding=utf-8
from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
