from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUsersForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'E-Mail'}),
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        # }

