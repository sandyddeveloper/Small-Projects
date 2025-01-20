from django.contrib import admin
from .models import CourseCategory, Course, Teacher, Schedule, StudentEnrollment

admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Schedule)
admin.site.register(StudentEnrollment)
