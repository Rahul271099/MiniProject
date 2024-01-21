from django.db import models
from Employee_Mangement.models import Employee

# Create your models here.
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return f'{self.employee.name}'