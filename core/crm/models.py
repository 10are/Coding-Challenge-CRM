# Create your models here.
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    verbose_name_plural = 'locations'


    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='department_manager')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    
    verbose_name_plural = 'departments'

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    
    verbose_name_plural = 'employees'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class TitleHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='title_history')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    
    verbose_name_plural = 'title history'
