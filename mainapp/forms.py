from django import forms 
from django.contrib.auth.models import User
from .models import * 
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'emailPopUp','placeholder': 'email или номер телефона'}),
            'password': forms.PasswordInput(attrs={'class': 'passwordPopUp', 'type': 'password', 'placeholder': 'Пароль'})
        }



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email или номер телефона'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']