from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createform(UserCreationForm):
    email = forms.EmailField(help_text="pls,enter a valid email")

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]