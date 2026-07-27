from django.db import models

# Create your models here.
class Student(models.Model):
    COURSE_CHOICES = [
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('Computer Science', 'Computer Science'),
        ('All subjects', 'All subjects'),
    ]

    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField()
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.name