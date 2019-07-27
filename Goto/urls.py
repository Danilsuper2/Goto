"""Goto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from myapp.views import win, alisa, alisa2, alisa0
from fix.views import main, log_in, reg, cab, like
from rost.views import api, api1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/api', api),
    path('you_win/', win),
    path('alisa/write/', alisa),
    path('alisa/read/', alisa2),
    path('alisa/new/', alisa0),
    path('fix/', main),
    path('fix/login/', log_in),
    path('fix/reg/', reg),
    path('fix/cab/', cab),
    path('fix/like/', like),
    path('api/', api1)
]
