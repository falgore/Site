# coding=utf-8
# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from Products.forms import ProductForm
from django.utils.translation import activate
activate('ru')


def index(request):
    print u'Hrllo'
    if request.method == 'POST':
        print request.POST
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('index.html', args)