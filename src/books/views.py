from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from . import models
import requests
from django.urls import reverse,reverse_lazy
from .models import Books,Binging,Author

class BooksCreate(CreateView):
    model=Books
    fields=('name','picture','price','author','genre','publishing_year','count_page','binging','format_book',
    'isbn','weight','age_limit','count_book','availability','rating','user')
    template_name='books/create.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})

class BooksDetail(DetailView):
    model= models.Books
    template_name='books/detail.html'

class BooksUpdate(UpdateView):
    model= Books
    fields=('name','picture','price','author','genre','publishing_year','count_page','binging','format_book',
    'isbn','weight','age_limit','count_book','availability','rating','user')
    template_name='books/update.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})


class BooksDelete(DeleteView):
    pass

class BooksList(ListView):
    pass