from django.contrib import admin

# Register your models here.
from .models import Department

class customDeapartment(admin.ModelAdmin):
    list_display = ['name','floor']


admin.site.register(Department,customDeapartment)
