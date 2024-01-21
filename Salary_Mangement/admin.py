from django.contrib import admin

# Register your models here.
from .models import EmployeeSalary

class customAdmin(admin.ModelAdmin):
    list_display = ['employee','salary','start_date','end_date']


admin.site.register(EmployeeSalary,customAdmin)