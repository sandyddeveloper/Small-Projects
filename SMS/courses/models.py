from django.db import models
from authentication.models import User  
import uuid


class CourseCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="courses")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15, unique=True, null=False, blank=False)
    expertise = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class CourseSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="schedules")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="schedules")
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.course.name} - {self.date} at {self.time}"


class StudentEnrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE, related_name="enrollments")
    acknowledged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.email} enrolled in {self.course.name}"