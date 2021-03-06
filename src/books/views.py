from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from . import models
import requests
from django.urls import reverse,reverse_lazy
from .models import Books,Binging,Author,Genre,Series,Publisher
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin



class BooksCreate(LoginRequiredMixin,CreateView):
    model=Books
    fields=('__all__')
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
        return form

class BooksDetail(DetailView):
    model= models.Books
    template_name='books/detail.html'



class BooksUpdate(LoginRequiredMixin,UpdateView):
    model= Books

    fields=('name','description','picture','price','author','genre','publisher','publishing_year','series','count_page','binging','format_book',
    'isbn','weight','age_limit','count_book','availability','rating')
    template_name='books/update.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_books:detail', kwargs={'pk':self.object.pk})



    def get_queryset(self,*args,**kwargs):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class BooksDelete(LoginRequiredMixin,DeleteView):
    model = Books
    template_name='books/delete.html'
    success_url =reverse_lazy('CRUDL_books:list')


class BooksList(ListView):
    model= models.Books
    template_name='books/list.html'
    paginate_by=4
    
    #накинуты права для Customers на просмотр только доступных книг
    def get_queryset(self,*args, **kwargs) :

        #получение назнавания группы для текущего авторизированного пользователя
        cust=self.request.user.groups.values_list('name', flat=True).first()
        print(cust)
        if self.request.user.groups.filter(name='Customers') or self.request.user.is_anonymous:
            print("группа текущего пользователя: ",cust )
            print("кастомера прост только активных")
            return self.model.objects.filter(availability=True).order_by('created')
        else:
            print("группа текущего пользователя: ",cust )
            return self.model.objects.all()





#genre CRUD

class GenreList(ListView):
    model=Genre
    template_name='genre/g_list.html'
    

        



class GenreDetail(DetailView):
    model=Genre
    template_name='genre/g_detail.html'


#author CRUD

class AuthorList(ListView):
    model=Author
    template_name='author/a_list.html'




class AuthorDetail(DetailView):
    model=Author
    template_name='author/a_detail.html'


# #Publisher
class PublisherList(ListView):
    model=Publisher
    template_name='publisher/p_list.html'



#Series
class SeriesList(ListView):
    model=Series
    template_name='series/se_list.html'




#набивание книгами
# def test():
#     for b in range(50):
#         Books(name=f"Books_{str(b)}",user_id=1).save()

# test()