#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# *******************************************
# -*- Time    : 2022/07/13 17:58:47
# -*- Author  : Allen_Jol
# -*- File    : urls.py
# *******************************************


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_simple_pwd', views.get_simple_pwd, name='get_simple_pwd'),
    path('get_complex_pwd', views.get_complex_pwd, name='get_complex_pwd'),
]
