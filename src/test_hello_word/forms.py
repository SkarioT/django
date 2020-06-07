from django import forms
from .models import Genre
from django.views.generic.base import TemplateView

class CreateGenreForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100
        )
    description = forms.CharField(
        label='Описание',
        max_length=100
        ) 

class CreateGenreFormModel(forms.ModelForm):
    class Meta:
        model= Genre
        fields =(
            'name',
            'description'
        )

