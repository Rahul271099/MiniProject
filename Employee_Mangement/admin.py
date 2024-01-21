from django.contrib import admin

# Register your models here.
from .models import Employee

class customAdmin(admin.ModelAdmin):
    list_display = ['name','designation','reporting_manager','department']


admin.site.register(Employee,customAdmin)
