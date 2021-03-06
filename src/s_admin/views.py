from django.shortcuts import render
#cart
from cart.models import BookInCart,Cart
#books
from books import models as books_model 
from books import views as book_view

#cart

from cart import models as cart_model

#order
from order.models import Order

#profile
from profiles.views import ProfilesDetail,ProfilesUpdate,ProfilesList
from profiles.models import Profile
from profiles.forms import CreateProfileFormModel
from django.contrib.auth.models import User

from django.core.exceptions import PermissionDenied
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView,TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime

# Create your views here.

#
# ДОДЕЛАТЬ ПРОВЕРКУ НА ПРОФИЛЬ, ТО ЧТО СЕЙЧАС - НЕ РАБОТАЕТ

class SAdminOrderList(LoginRequiredMixin,ListView):
    model=Order
    template_name='s_admin/order/o_list.html'

    def get_queryset(self,*args,**kwargs):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminOrderUpdate(LoginRequiredMixin,UpdateView):
    model=Order
    template_name='s_admin/order/o_update.html'
    fields=('status2','delivery_address','contact_phone','comment')

    def get_object(self, queryset=None):
        obj=super().get_object(queryset=queryset)
        global cur_comment
        cur_comment=obj.comment
        # order=Order.objects.get(pk=cur_order)
        # print('get_obj_comen',order.comment)
        return obj

    def get_success_url(self):
        user=self.request.user
        cdt=datetime.now()
        cdt=datetime.strftime(cdt,'%d.%m.%Y, %H:%M')
        cur_order=self.object.pk
        order=Order.objects.get(pk=cur_order)
        print(order.comment)
        comment=cur_comment+'\n'+str(cdt)+' '+str(user)+':\n'+str(order.comment)
        order=Order.objects.filter(pk=cur_order).update(comment=comment)

        return reverse_lazy('s-admin:order')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class S_Admin(LoginRequiredMixin,ListView):
    model=Order
    template_name='s_admin/index.html'
    context_object_name = "orders"

    def get_context_data(self,**kwargs):
        i=0
        j=0
        b=0
        k=0
        context = super().get_context_data(**kwargs)
        orders=Order.objects.all()
        for order in orders:
            if order.status2=='Отменен':
                i+=1
                context['canseled']=i
            if order.status2=='Доставка':
                j+=1
                context['delivery']=j
            if order.status2=='В обработке':
                b+=1
                context['inprog']=b
            if order.status2=='Выполнен':
                k+=1
                context['success']=k
      
        return context

    def render_to_response(self, context, **response_kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            raise PermissionDenied
        return super().render_to_response(context, **response_kwargs)    



class CustomersList(ProfilesList):
    template_name='s_admin/customers/list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class CustomersUpdate(ProfilesUpdate):
    template_name='s_admin/customers/update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:customers')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class CustomersDetail(ProfilesDetail):
    template_name='s_admin/customers/detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

#product|books CRUDL for S-Admin portal
class SAdminBooksList(LoginRequiredMixin,book_view.BooksList):
    template_name='s_admin/books/b_list.html'
    paginate_by=None
    paginate_by=4
    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminBooksDetail(LoginRequiredMixin,book_view.BooksDetail):
    template_name='s_admin/books/b_detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminBooksDelete(book_view.BooksDelete):
    template_name='s_admin/books/b_delete.html'
    success_url =reverse_lazy('s-admin:books')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminBooksUpdate(book_view.BooksUpdate):
    template_name='s_admin/books/b_update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:books_detail', kwargs={'pk':self.object.pk})

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminBooksCreate(book_view.BooksCreate):
    template_name='s_admin/books/b_create.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:books_detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return super().get_context_data(**kwargs)

#genre CRUD
class SAdminGenreCreate(LoginRequiredMixin,CreateView):
    model=books_model.Genre
    fields=('__all__')
    template_name='s_admin/genre/g_create.html'
    success_url =reverse_lazy('s-admin:genre')

    def get_context_data(self, **kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return super().get_context_data(**kwargs)


class SAdminGenreList(LoginRequiredMixin,ListView):
    model=books_model.Genre
    template_name='s_admin/genre/g_list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
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
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 
class SAdminGenreDetail(LoginRequiredMixin,DetailView):
    model=books_model.Genre
    template_name='s_admin/genre/g_detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminGenreDelete(LoginRequiredMixin,DeleteView):
    model=books_model.Genre
    template_name='s_admin/genre/g_delete.html'
    success_url =reverse_lazy('s-admin:genre')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
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

    def get_context_data(self, **kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return super().get_context_data(**kwargs)


class SAdminAuthorList(LoginRequiredMixin,ListView):
    model=books_model.Author
    template_name='s_admin/author/a_list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
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
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 
class SAdminAuthorDetail(LoginRequiredMixin,DetailView):
    model=books_model.Author
    template_name='s_admin/author/a_detail.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminAuthorDelete(LoginRequiredMixin,DeleteView):
    model=books_model.Author
    template_name='s_admin/author/a_delete.html'
    success_url =reverse_lazy('s-admin:author')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
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
        print(self.request.user.groups.get())
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
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 





#publisher
class SAdminPublisherCreate(LoginRequiredMixin,CreateView):
    fields=('__all__')
    model=books_model.Publisher
    template_name='s_admin/publisher/p_create.html'
    success_url =reverse_lazy('s-admin:publisher')

    def get_context_data(self, **kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return super().get_context_data(**kwargs)
class SAdminPublisherList(LoginRequiredMixin,ListView):
    model=books_model.Publisher
    template_name='s_admin/publisher/p_list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 
class SAdminPublisherUpdate(LoginRequiredMixin,UpdateView):
    model=books_model.Publisher
    fields=('__all__')
    template_name='s_admin/publisher/p_update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:publisher')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminPublisherDelete(LoginRequiredMixin,DeleteView):
    model=books_model.Publisher
    template_name='s_admin/publisher/p_delete.html'
    success_url =reverse_lazy('s-admin:publisher')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

#series
class SAdminSeriesCreate(LoginRequiredMixin,CreateView):
    fields=('__all__')
    model=books_model.Series
    template_name='s_admin/series/se_create.html'
    success_url =reverse_lazy('s-admin:series')

    def get_context_data(self, **kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return super().get_context_data(**kwargs)
class SAdminSeriesList(LoginRequiredMixin,ListView):
    model=books_model.Series
    template_name='s_admin/series/se_list.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 
class SAdminSeriesUpdate(LoginRequiredMixin,UpdateView):
    model=books_model.Series
    template_name='s_admin/series/se_update.html'
    fields=('__all__')
    def get_success_url(self):
        return reverse_lazy('s-admin:series')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups)
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 

class SAdminSeriesDelete(LoginRequiredMixin,DeleteView):
    model=books_model.Series
    template_name='s_admin/series/se_delete.html'
    success_url =reverse_lazy('s-admin:series')

    def get_queryset(self,*args,**kwargs):
        print(self.request.user.groups.get())
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all() 


