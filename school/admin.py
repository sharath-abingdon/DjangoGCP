from django.contrib import admin
from .models import Teacher
from .models import Student
from .models import Classroom
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Classroom)