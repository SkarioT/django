from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from . import models
import requests
from django.urls import reverse,reverse_lazy
from .models import Books,Binging,Author
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin



class BooksCreate(LoginRequiredMixin,CreateView):
    model=Books
    fields=('name','picture','price','author','genre','publishing_year','count_page','binging','format_book',
    'isbn','weight','age_limit','count_book','availability','rating','user')
    template_name='books/create.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})
    
#подкидываю по умочанию пользователя текущего
    def get_initial(self):
        initinal=super().get_initial()
        user=self.request.user
        prof_user=Profile.objects.get(username=user)
        initinal['user']=prof_user.pk
        return initinal
#скрываю возможность сменить пользователя(визуально)    
    def get_form(self, form_class=None):
        form=super().get_form(form_class=form_class)
        form.fields['user'].widget.attrs.update({"class": "d-none"})
        form.fields['user'].widget.attrs.update({"":""})
        return form

class BooksDetail(LoginRequiredMixin,DetailView):
    model= models.Books
    template_name='books/detail.html'

    def get_context_data(self, **kwargs):
        c= super().get_context_data(**kwargs)
        try:
            user=self.request.user
            prof_user=Profile.objects.get(username=user)
            print(user)
            print(prof_user.pk)
            c['prof_user']=prof_user.pk
        except Profile.DoesNotExist:
            prof_user=None
        return c

class BooksUpdate(LoginRequiredMixin,UpdateView):
    model= Books

    fields=('name','picture','price','author','genre','publishing_year','count_page','binging','format_book',
    'isbn','weight','age_limit','count_book','availability','rating','user')
    template_name='books/update.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        c= super().get_context_data(**kwargs)
        try:
            user=self.request.user
            prof_user=Profile.objects.get(username=user)
            print(user)
            print(prof_user.pk)
            c['prof_user']=prof_user.pk
        except Profile.DoesNotExist:
            prof_user=None
        return c

class BooksDelete(LoginRequiredMixin,DeleteView):
    model = Books
    template_name='books/delete.html'
    success_url =reverse_lazy('CRUDL_books:list')


class BooksList(LoginRequiredMixin,ListView):
    model= models.Books
    template_name='books/list.html'
    #накинуты права для Customers на просмотр только доступных книг
    def get_queryset(self,*args, **kwargs) :
        print("group:",self.request.user.groups.filter(name='Customers'))
        #получение назнавания группы для текущего авторизированного пользователя
        cust=self.request.user.groups.values_list('name', flat=True).first()
        print(cust)
        if self.request.user.has_perm('books.view_books') and self.request.user.groups.filter(name='Staff') :
            return self.model.objects.filter(availability=True)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        c= super().get_context_data(**kwargs)
        try:
            user=self.request.user
            prof_user=Profile.objects.get(username=user)
            print(user)
            print(prof_user.pk)
            c['prof_user']=prof_user.pk
        except Profile.DoesNotExist:
            prof_user=None
        return c
            



class Home_page(ListView):
    model= models.Books
    template_name='books/home_page.html'
    paginate_by=8
    
    def get_context_data(self, **kwargs):
        book_pk=self.request.GET.get('book_pk')
        print("book_pk:",book_pk)
        c= super().get_context_data(**kwargs)
        c['book_pk']=book_pk
         #подкидуываю в контектс для каждого обработчика в контект Profile user pk
        try:
            user=self.request.user
            prof_user=Profile.objects.get(username=user)
            print(user)
            print(prof_user.pk)
            c['prof_user']=prof_user.pk
        except Profile.DoesNotExist:
            prof_user=None
        return c

#набивание книгами
# def test():
#     for b in range(50):
#         Books(name=f"Books_{str(b)}",user_id=1).save()

# test()