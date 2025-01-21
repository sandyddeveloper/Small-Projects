from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def admin_dashboard(request):
    return render(request, "panel/admin_dashboard.html")


@login_required
def student_dashboard(request):
    return render(request, "panel/student_dashboard.html")