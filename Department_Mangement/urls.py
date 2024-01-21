from django.urls import path
from .views import *

urlpatterns = [
    path('data/',department_list, name='department_list'),
    path('salary_report/', department_salary_costs, name='salary_report'),
]