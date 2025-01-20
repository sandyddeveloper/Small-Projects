from django.urls import path
from .views import register, user_login, user_logout
from core.views import admin_dashboard, student_dashboard

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("student/dashboard/", student_dashboard, name="student_dashboard"),
]
