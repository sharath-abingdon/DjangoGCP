from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.EmailField()
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.EmailField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    
class Classroom(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student')
    class_code = models.CharField(max_length=10)