from django import forms
from .models import Profile
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User


class CreateProfileFormModel(forms.Form):
    username = forms.CharField(
        label='Лоигн',
        max_length=15
    )
    password=forms.CharField(
        label='Пароль',
        max_length=15,
        widget=forms.PasswordInput
    )
    email=forms.EmailField(
        label='email',
        max_length=15,
        
    )
    first_name=forms.CharField(
        label='Имя',
        max_length=15,
        required=None
    )
    last_name=forms.CharField(
        label='Фамилия',
        max_length=15,
        required=None 
    )
    phone=forms.CharField(
        label='Телефон',
        max_length=15
    )
    class Meta:
        model= User
        fields=('username','password','first_name','last_name','email')
