"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from application.views import index
from application.views import page1
from application.views import page2
from application.views import page3
from application.views import candidature
from application.views import merci

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('page1/', page1),
    path('page2/', page2),
    path('page3/', page3),
    path('candidature/', candidature),
    path('merci/', merci)
]
