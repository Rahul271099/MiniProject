from django.urls import path
from .views import *

urlpatterns = [
    path('data/',Salary_list, name='salary_list'),
]