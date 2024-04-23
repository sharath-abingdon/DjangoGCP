from django.urls import path, include
from .views import student_new

urlpatterns = [
    path('new/', student_new, name='student_new'),
]
