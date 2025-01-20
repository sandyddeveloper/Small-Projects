from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  
    email = models.EmailField(unique=True)  # Ensure email is unique
    role = models.CharField(max_length=10, choices=[("admin", "Admin"), ("student", "Student")])

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["username"]  

    def __str__(self):
        return self.email


