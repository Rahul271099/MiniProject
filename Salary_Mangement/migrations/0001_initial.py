# Generated by Django 5.0.1 on 2024-01-21 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee_Mangement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee_Mangement.employee')),
            ],
        ),
    ]
