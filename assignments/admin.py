from django.contrib import admin
from .models import Teacher, Student, Lesson, Assignment

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Assignment)