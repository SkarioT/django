from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from . import models
import requests
from django.urls import reverse,reverse_lazy
from .models import Books,Binging,Author
from django.contrib.auth.mixins import LoginRequiredMixin


def home_page(request):
    context={}
    return render(request, template_name="books/home_page.html", context={})

class BooksCreate(LoginRequiredMixin,CreateView):
    model=Books
    fields=('name','picture','price','author','genre','publishing_year','count_page','binging','format_book',
    'isbn','weight','age_limit','count_book','availability','rating','user')
    template_name='books/create.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})
    def get_context_data(self, **kwargs):
        print(self.request.user)
        return super().get_context_data(** kwargs)

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
class BooksDetail(LoginRequiredMixin,DetailView):
    model= models.Books
    template_name='books/detail.html'
 

class BooksUpdate(LoginRequiredMixin,UpdateView):
    model= Books

    fields=('name','picture','price','author','genre','publishing_year','count_page','binging','format_book',
    'isbn','weight','age_limit','count_book','availability','rating','user')
    template_name='books/update.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})



class BooksDelete(LoginRequiredMixin,DeleteView):
    model = Books
    template_name='books/delete.html'
    success_url =reverse_lazy('CRUDL_books:list')


class BooksList(LoginRequiredMixin,ListView):
    model= models.Books
    template_name='books/list.html'
    #накинуты права для стафюзер на просмотр только доступных книг
    def get_queryset(self,*args, **kwargs) :
        print(self.request.user.groups.filter(name='Customers'))
        #получение назнавания группы для текущего авторизированного пользователя
        cust=self.request.user.groups.values_list('name', flat=True).first()
        print(cust)
        if self.request.user.has_perm('books.view_books') and self.request.user.groups.filter(name='Staff') :
            return self.model.objects.filter(availability=True)
        else:
            return self.model.objects.all()


class Home_page(ListView):
    model= models.Books
    template_name='books/home_page.html'
    paginate_by=8

#набивание книгами
# def test():
#     for b in range(50):
#         Books(name=f"Books_{str(b)}",user_id=1).save()

# test()