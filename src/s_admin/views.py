from django.shortcuts import render
#cart
from cart.models import BookInCart,Cart
#books
from books import models as books_model 
from books import views as book_view

#cart

from cart import models as cart_model


#profile
from profiles.views import ProfilesDetail,ProfilesUpdate,ProfilesList
from profiles.models import Profile
from profiles.forms import CreateProfileFormModel
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView,TemplateView

# Create your views here.

#
# ДОДЕЛАТЬ ПРОВЕРКУ НА ПРОФИЛЬ, ТО ЧТО СЕЙЧАС - НЕ РАБОТАЕТ

class S_Admin(LoginRequiredMixin,TemplateView):
    models=books_model.Books
    template_name='s_admin/index.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class CustomersList(ProfilesList):
    template_name='s_admin/customers/list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class CustomersUpdate(ProfilesUpdate):
    template_name='s_admin/customers/update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:customers')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class CustomersDetail(ProfilesDetail):
    template_name='s_admin/customers/detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

#product|books CRUDL for S-Admin portal
class SAdminBooksList(book_view.BooksList):
    template_name='s_admin/books/b_list.html'
    paginate_by=None
    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminBooksDetail(book_view.BooksDetail):
    template_name='s_admin/books/b_detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminBooksDelete(book_view.BooksDelete):
    template_name='s_admin/books/b_delete.html'
    success_url =reverse_lazy('s-admin:product')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminBooksUpdate(book_view.BooksUpdate):
    template_name='s_admin/books/b_update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:books_detail', kwargs={'pk':self.object.pk})

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminBooksCreate(book_view.BooksCreate):
    template_name='s_admin/books/b_create.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:books_detail', kwargs={'pk':self.object.pk})

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

#genre CRUD
class SAdminGenreCreate(LoginRequiredMixin,CreateView):
    model=books_model.Genre
    fields=('__all__')
    template_name='s_admin/genre/g_create.html'
    success_url =reverse_lazy('s-admin:genre')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminGenreList(LoginRequiredMixin,ListView):
    model=books_model.Genre
    template_name='s_admin/genre/g_list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminGenreUpdate(LoginRequiredMixin,UpdateView):
    model=books_model.Genre
    fields=('__all__')
    template_name='s_admin/genre/g_update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:genre_detail', kwargs={'pk':self.object.pk})

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 
class SAdminGenreDetail(LoginRequiredMixin,DetailView):
    model=books_model.Genre
    template_name='s_admin/genre/g_detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminGenreDelete(LoginRequiredMixin,DeleteView):
    model=books_model.Genre
    template_name='s_admin/genre/g_delete.html'
    success_url =reverse_lazy('s-admin:genre')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

#author CRUD
class SAdminAuthorCreate(LoginRequiredMixin,CreateView):
    model=books_model.Author
    fields=('__all__')
    template_name='s_admin/author/a_create.html'
    success_url =reverse_lazy('s-admin:author')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminAuthorList(LoginRequiredMixin,ListView):
    model=books_model.Author
    template_name='s_admin/author/a_list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminAuthorUpdate(LoginRequiredMixin,UpdateView):
    model=books_model.Author
    fields=('__all__')
    template_name='s_admin/author/a_update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:author_detail', kwargs={'pk':self.object.pk})

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 
class SAdminAuthorDetail(LoginRequiredMixin,DetailView):
    model=books_model.Author
    template_name='s_admin/author/a_detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminAuthorDelete(LoginRequiredMixin,DeleteView):
    model=books_model.Author
    template_name='s_admin/author/a_delete.html'
    success_url =reverse_lazy('s-admin:author')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

#cart view

class SAdminCartList(LoginRequiredMixin,ListView):
    model=cart_model.Cart
    template_name='s_admin/cart/c_list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminCartUpdate(LoginRequiredMixin,UpdateView):
    model=cart_model.Cart
    fields=('__all__')
    template_name='s_admin/cart/c_update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:cart_detail', kwargs={'pk':self.object.pk})

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 
class SAdminCartDetail(LoginRequiredMixin,DetailView):
    model=cart_model.Cart
    template_name='s_admin/cart/c_detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminCartDelete(LoginRequiredMixin,DeleteView):
    model=Cart
    template_name='s_admin/cart/c_delete.html'
    success_url =reverse_lazy('s-admin:cart')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 





