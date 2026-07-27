from django.shortcuts import render,redirect
from django.http import HttpResponse

from school.forms import StudentForm
from .models import Student


# Create your views here.
# def student_list(request):
#     students = Student.objects.all()
#     context = {
#         'students': students
#     }
#     return render(request,'student_list.html',context )

def home(request):
    return render(request, 'home.html')

def admin_view(request):
    students = Student.objects.all()
    return render(request, 'admin_view/admin.html', {
        'students': students
    })
    
    
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_view')
    else:
        form = StudentForm()

    return render(request, 'admin_view/add_student.html', {
        'form': form
    })

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('admin_view')
    else:
        form = StudentForm(instance=student)

    return render(request, 'admin_view/edit_student.html', {
        'form': form
    })
    
    
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('admin_view')

    return render(request, 'admin_view/delete_student.html', {
        'student': student
    })

def student_view(request):
    students = Student.objects.all()

    return render(request, 'student_view/student_view.html', {
        'students': students
    })
    
