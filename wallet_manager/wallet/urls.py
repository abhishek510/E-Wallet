from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    path('index', index, name = 'index'),
    path('modfiy', modifybalance, name = 'modifybalance'),
    path('test', test, name = 'test'),
    ]