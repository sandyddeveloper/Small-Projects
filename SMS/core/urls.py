from django.urls import path
from .views import admin_dashboard, student_dashboard

urlpatterns = [

    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("student/dashboard/", student_dashboard, name="student_dashboard"),
]
