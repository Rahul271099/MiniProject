from django.db import models
from Department_Mangement.models import Department

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    designation = models.CharField(max_length=20, choices=[('Associate', 'Associate'), ('TL', 'TL'), ('Manager', 'Manager')])
    reporting_manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'


