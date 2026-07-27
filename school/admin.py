from django.contrib import admin
from .models import Student
# Register your models here.
class adminStudent(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'email', 'course', 'enrollment_date')
admin.site.register(Student, adminStudent)