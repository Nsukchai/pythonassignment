from django.db import models

# Create your models here.

class Status(models.Model):
    status_choices = [
        ('recruit', 'in recruitment process'),
        ('onboarding', 'waiting for onboarding'),
        ('probation', 'in probation period'),
        ('normal', 'normal'),
        ('resigned', 'resigned')
    ]
    status_name = models.CharField(choices=status_choices, max_length=20, default='normal')
    
    def __str__(self):
        return self.get_status_name_display()

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    manager = models.BooleanField()  
    status = models.ForeignKey(Status, on_delete=models.CASCADE)  
    image = models.ImageField(upload_to='employee_images/')  

    def __str__(self):
        return self.name

class Position(models.Model):
    position_name = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.position_name

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    manager = models.ForeignKey(Employee, related_name='manages_department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.department_name

