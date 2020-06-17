from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from . import models

class BooksCreate(CreateView):
    pass

class BooksDetail(DetailView):
    model= models.Books
    template_name='books/detail.html'
    #template_name='test_hello_word/detail.html'

class BooksUpdate(UpdateView):
    pass

class BooksDelete(DeleteView):
    pass

class BooksList(ListView):
    pass