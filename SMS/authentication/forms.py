from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# User Registration Form (For Students)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

# Login Form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Username")
    email = forms.EmailField()
