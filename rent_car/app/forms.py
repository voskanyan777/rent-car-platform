from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'your email', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'your login', 'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'your password', 'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'repeat password', 'class': 'form-control'}),
        }
