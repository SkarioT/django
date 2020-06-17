from django import forms
from .models import Books,Binging,Author
from django.views.generic.base import TemplateView

class CreateBooksForm(forms.Form):
    name = forms.CharField(
        label='Название книги',
        max_length=100
        )

    #picture

    price = forms.CharField(
        label='Цена',
        max_length=100
        )
    author=forms.(
        'Author',
        verbose_name="Автор"
    ) 
    #seria

    publishing_yar= forms.IntegerField(
        label='Год издания'

    )

class CreateBooksFormModel(forms.ModelForm):
    class Meta:
        model= Genre
        fields =(
            'name',
            'description'
        )

