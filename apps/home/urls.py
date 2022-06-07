# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from apps.home import views
from django.contrib import admin
admin.site.site_header = 'SUSCO BOT PAGE ADMIN'
admin.site.site_title = 'SUSCO BOT PAGE ADMIN'

urlpatterns = [

    re_path(r'^.*\.html', views.pages, name='pages'),
    path('', views.index, name='home'),
    path('linebot/', include('line_bot.urls')),
    path('liffmainpage+<str:userId>/',views.liffmainpage,name='liffmainpage'),

]
