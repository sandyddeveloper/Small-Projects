from django.shortcuts import render

def admin_dashboard(request):
    return render(request, "panel/admin_dashboard.html")

def student_dashboard(request):
    return render(request, "panel/student_dashboard.html")