from django.db import models
from authentication.models import User  

class CourseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    expertise = models.CharField(max_length=255, help_text="Subject expertise")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="courses")
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedules')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.course.name} - {self.date} {self.time}"
class StudentEnrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='enrollments')
    acknowledged = models.BooleanField(default=False)  # Acknowledgment feature

    def __str__(self):
        return f"{self.student.username} - {self.course.name} ({'Acknowledged' if self.acknowledged else 'Pending'})"
