# stores all the forms we need
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from static_pages.models import InstaUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstaUser
        fields = ['username','email','profile_img']