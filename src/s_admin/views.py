from django.shortcuts import render
#cart
from cart.models import BookInCart,Cart
#books
from books.models import Books 
from books import views as book_view



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

class S_Admin(LoginRequiredMixin,TemplateView):
    models=Books
    template_name='s_admin/index.html'

class CustomersList(ProfilesList):
    template_name='s_admin/customers/list.html'

class CustomersUpdate(ProfilesUpdate):
    template_name='s_admin/customers/update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:customers')

class CustomersDetail(ProfilesDetail):
    template_name='s_admin/customers/detail.html'


class ProductList(book_view.BooksList):
    template_name='s_admin/product/p_list.html'


class ProductBookDetail(book_view.BooksDetail):
    template_name='s_admin/product/b_detail.html'

class ProductBookDelete(book_view.BooksDelete):
    template_name='s_admin/product/b_delete.html'
    success_url =reverse_lazy('s-admin:product')




