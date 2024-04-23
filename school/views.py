from django.shortcuts import render
from .forms import StudentForm
from django.http import JsonResponse

def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return JsonResponse({'message': 'Student added successfully'}, status=201)
    else:
        form = StudentForm()
        return render(request, 'student_add.html', {'form': form})
