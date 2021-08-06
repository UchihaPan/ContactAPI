"""contactapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:
"""
from django.contrib import admin
from django.urls import path,include
from .views import signupview,createcontactapiview,detailcontactapiview,contactapiview

urlpatterns = [
    path('signup/', signupview.as_view(),name='signup'),
    path('create/', createcontactapiview.as_view(), name='create'),
    path('', contactapiview.as_view(), name='list'),

    path('detail/<int:id>/', detailcontactapiview.as_view(), name='detail'),
   path('auth/', include('rest_framework.urls')),

]
