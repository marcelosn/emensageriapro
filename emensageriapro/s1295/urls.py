#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1295-iderespinf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1295.views.s1295_iderespinf.apagar', 
        name='s1295_iderespinf_apagar'),

url(r'^s1295-iderespinf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1295.views.s1295_iderespinf.listar', 
        name='s1295_iderespinf'),

url(r'^s1295-iderespinf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1295.views.s1295_iderespinf.salvar', 
        name='s1295_iderespinf_salvar'),





)