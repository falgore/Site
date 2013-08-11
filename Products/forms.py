# coding=utf-8
from bootstrap_toolkit.widgets import BootstrapUneditableInput, BootstrapTextInput
from django import forms
from Products.models import *

class ProductForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        help_text=u'I am uneditable and you cannot enable me with JS',
        initial=u'Uneditable',
        widget=BootstrapTextInput(prepend='asjdas'),
        label='Иня'
    )

    class Meta:
        model = Products
        #fields = ('name', )