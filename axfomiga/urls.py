"""axfomiga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/',views.main),
    url(r'^index/',views.index),
    url(r'^market/',views.market),
    url(r'^cart/',views.shopcar),
    url(r'^mine/',views.mine),

    url(r'^regist/',views.regist),
    url(r'^login/',views.login),

    url(r'^getyzm/',views.getyzm),

    url(r'^nameyjy/',views.nameyjy),
    url(r'^codejy/',views.codejy),

    url(r'^addshopcar/', views.addshopcar),
    url(r'^subshopcar/', views.subshopcar),
    url(r'^selshopcar/', views.selshopcar),

    url(r'^changeall/',views.changeall),
    url(r'^changeone/',views.changeone),

    url(r'^jiesuan/',views.jiesuan)




]
