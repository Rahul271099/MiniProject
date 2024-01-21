from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from datetime import datetime
from .models import *
from Department_Mangement.models import Department
from Salary_Mangement.models import EmployeeSalary
from .forms import SalaryReportform
# Create your views here.
def department_list(request):
    department = Department.objects.all()

    context ={
        "dData":department
    }
    return render(request,"list.html",context)



def department_salary_costs(request):
    if request.method == 'POST':
        form =SalaryReportform(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Query to get department-wise sum of salaries
            department_salaries = EmployeeSalary.objects.filter(
                start_date__lte=end_date,
                end_date__gte=start_date
            ).values('employee__department__name').annotate(total_salary=models.Sum('salary'))

            return render(request, 'departmentsalarycost.html', {'department_salaries': department_salaries})

    else:
        form =SalaryReportform()

    return render(request, 'departmentSalaryCostfrom.html', {'form': form})

