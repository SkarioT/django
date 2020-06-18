from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from . import models
import requests
from django.urls import reverse,reverse_lazy
from .models import Books,Binging,Author


def home_page(request):
    context={}
    return render(request, template_name="books/home_page.html", context={})

class BooksCreate(CreateView):
    model=Books
    fields=('name','picture','price','author','genre','publishing_year','count_page','binging','format_book',
    'isbn','weight','age_limit','count_book','availability','rating','user')
    template_name='books/create.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})

#create with update
# class BooksCreate(UpdateView):
#     model= Books
#     fields=('name','picture','price','author','genre','publishing_year','count_page','binging','format_book',
#     'isbn','weight','age_limit','count_book','availability','rating','user')
#     template_name='books/update.html'

#     def get_success_url(self):
#         return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})
#     def get_object(self):
#         print(self.kwargs)
#     #     obj, created = self.objects.get_or_create(first_name='John',last_name='Lennon',defaults={'birthday': date(1940, 10, 9)}
#     #     return obj
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
    model = Books
    template_name='books/delete.html'
    success_url =reverse_lazy('CRUDL_books:list')

class BooksList(ListView):
    model= models.Books
    template_name='books/list.html'

class Home_page(ListView):
    model= models.Books
    template_name='books/home_page.html'


