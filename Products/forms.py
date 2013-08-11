# coding=utf-8
from django import forms
from Products.models import *


class ProductForm(forms.ModelForm):
    #name = forms.CharField(max_length=100)

    class Meta:
        model = Products
        #fields = ('name', )