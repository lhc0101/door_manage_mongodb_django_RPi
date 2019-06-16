"""ComplaintDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 导入对应 app 的 views 文件
from cmdb  import views
urlpatterns = [
    path('index/',views.index),
    path('',views.index),
    path('query',views.query),
     # path('queryshow',views.queryshow),
    path('toAdd/',views.toAdd),
    path('addInvitation/',views.addInvitation),
    path('toUpdate/',views.toUpdate),
    path('toquery/',views.toquery),
    path('updateInvitation/',views.updateInvitation),
    path('delete/',views.delete),
    path('logs/',views.logs),
    path('logtoquery/',views.logtoquery),
    path('logquery/',views.logquery),


]
