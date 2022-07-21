# -*- coding: utf-8 -*-
#
from django.urls import path
import django_cas_ng.views
from . import views

urlpatterns = [
    path('login/', views.CasAuthRequestView.as_view(), name='cas-login'),
    path('logout/', django_cas_ng.views.LogoutView.as_view(), name='cas-logout'),
    path('callback/', django_cas_ng.views.CallbackView.as_view(), name='cas-proxy-callback'),
]
