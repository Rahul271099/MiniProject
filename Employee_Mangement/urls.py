from django.urls import path
from .views import *

urlpatterns = [
    path('data/',employee_list, name='employee_list'),
]