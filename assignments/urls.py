from django.urls import path
from . import views

urlpatterns = [
    path('assignments/', views.assign_lesson),
    path('students/<int:student_id>/assignments/', views.student_assignments),
    path('assignments/<int:assignment_id>/complete/', views.mark_complete),
    path('teachers/<int:teacher_id>/assignments/status/', views.teacher_assignment_status),
]