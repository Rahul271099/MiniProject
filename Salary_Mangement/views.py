from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def Salary_list(request):
    emp_salaries = EmployeeSalary.objects.all()

    context = {
        "emp_salary":emp_salaries
    }
    return render(request,"list.html",context)