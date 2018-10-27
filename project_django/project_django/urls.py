"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from aplication_1.views import Model1View, Model1ViewCreate, MainPageView, Model2View, Model1ViewDelete, Model1ViewUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main-page'),
    path('model1/', Model1View.as_view(), name='model1-list'),
    path('model2/', Model2View.as_view(), name='model2-list'),
    path('model1create/', Model1ViewCreate.as_view(), name='model1-create'),
    path('model1delete/<pk>', Model1ViewDelete.as_view(), name='model1-delete'),
    path('model1update/<pk>', Model1ViewUpdate.as_view(), name='model1-update'),
]
