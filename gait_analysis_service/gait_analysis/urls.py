# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from gait_analysis_service.gait_analysis import views

urlpatterns = [
    url(r'^detail/$', views.detail),
    url(r'^index/$', views.main_page),
    url(r'^update$', views.data_upload),
    url(r'^record/$', views.record),
    url(r'^record_query/$', views.record_query),
    url(r'^main_query/$', views.main_query),
    url(r'^updateTest/$', views.updateTest),
]

