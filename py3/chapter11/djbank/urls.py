from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^$', 'djbank.views.index_view', name='index'),
    url(r'^pay/$', 'djbank.views.pay_view', name='pay'),
    url(r'^logout/$', 'djbank.views.logout_view'),
    )
