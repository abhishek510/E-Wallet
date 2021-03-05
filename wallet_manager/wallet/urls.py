from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    path('index', index, name = 'index'),
    path('modify', test, name = 'test'),
    path('show_balance', show_balance, name = 'show_balance'),
    path('transaction_history', transaction_history, name = 'transaction_history'),
    ]