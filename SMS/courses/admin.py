from django.contrib import admin
from .models import  CourseCategory, Course, Teacher, CourseSchedule, StudentEnrollment

admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(CourseSchedule)
admin.site.register(StudentEnrollment)
