from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def employee_list(request):
    employee_data = Employee.objects.all()

    context = {
        "employee":employee_data
    }

    return render(request,"employee_list.html",context)