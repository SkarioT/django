from django import forms
from .models import Profile
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField


class CreateProfileFormModel(forms.Form):
    username = forms.CharField(
        label='Лоигн',
        max_length=15
    )
    password=forms.CharField(
        label='Пароль',
        max_length=20,
        widget=forms.PasswordInput
    )
    email=forms.EmailField(
        label='email',
        max_length=45,
        
    )
    # phone=forms.CharField(
    #     label='Телефон',
    #     max_length=15
    # )
    phone=PhoneNumberField(
       label='Телефон',
    )
    first_name=forms.CharField(
        label='Имя',
        max_length=25,
        required=None
    )
    last_name=forms.CharField(
        label='Фамилия',
        max_length=25,
        required=None 
    )
    address_1 = forms.CharField(
        label="Адрес 1",
        max_length=128,
        required=None 
    )
    address_2 = forms.CharField(
        label="Адрес 2",
        max_length=128,
        required=None 
    )
    city = forms.CharField(
        label="Город",
        max_length=64,
        required=None 
    )
    county = forms.CharField(
        label="Страна",
        max_length=64,
        required=None 

    )
    zip_code = forms.CharField(
        label="Почтовый индекс",
        max_length=5,
        required=None 
    )

    class Meta:
        model= User
        fields=('username','password','first_name','last_name','email')
