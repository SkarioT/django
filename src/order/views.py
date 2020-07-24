from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from profiles.models import Profile
from books.models import Books
from cart.models import Cart,BookInCart
from .models import Order
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from datetime import datetime
# Create your views here.

# Create your views here.

class CreateOrder(SuccessMessageMixin,UpdateView):
    model=Order
    context_object_name='order'
    template_name="order/create.html"
    fields=('delivery_address','contact_phone','comment')


    def get_object(self, queryset=None):
        #набросок для заполнения данными из юзера поля телефон и  адрес 
        try:
            user=self.request.user
            print(user)
            prof_user=Profile.objects.get(username=user)
        except Profile.DoesNotExist:
            prof_user=None
        # print(prof_user.is_anonymous)
        if prof_user == None:
            print("prof_user is none",prof_user)
            delivery_address1="Please fill in"
            contact_phone="Please fill in"
        else:
            delivery_address1=prof_user.address_1
            contact_phone=prof_user.phone

        #получаю корзину
        cart_pk=self.request.session.get('cart_pk')
        print('cart_pk:',cart_pk)

        cart=Cart.objects.get(pk=cart_pk)

        order_pk=cart.pk
   

        obj,created=self.model.objects.get_or_create(
            pk=order_pk,
            defaults={
                'cart' :cart,
                'status': False,
                'delivery_address': delivery_address1,
                'contact_phone': contact_phone,  
            }
            )

        return obj

    def get_success_url(self):

        #пример нотификации если заказ офоромлен
        # notify_managers(self.request.user, self.object)
        cart_pk=self.request.session['cart_pk']
        del(self.request.session['cart_pk'])
        if self.request.user.is_anonymous:
            user='Гость'
        else:
            user=self.request.user
        print(user)
       
        #получаю список книг корзине исходя из ид корзины
        booksincart = BookInCart.objects.all().filter(cart = cart_pk)
        print("books",booksincart.all())
        for book in booksincart:
            print("book: ",book.books.pk)
            cur_book=Books.objects.filter(pk=book.books.pk).last()
            print("Всего книг",cur_book.count_book)
            print("Книг в заказе",book.qantity)

            new_count=int(cur_book.count_book)- int(book.qantity)
            cur_book.count_book=new_count
            print("cur_book qantity past update",cur_book.count_book)
            cur_book.save()
            #проверю, если книг остаётся 0 - перевочу книгу(и) в неактивные
            if cur_book.count_book == 0:
                cur_book.availability=False
                cur_book.save()

        
        cdt=datetime.now()
        cdt=datetime.strftime(cdt,'%d.%m.%Y, %H:%M')
        cur_order=self.object.pk
        order=Order.objects.get(pk=cur_order)
        print(order.comment)
        comment=str(cdt)+' '+str(user)+':\n'+str(order.comment)
        order=Order.objects.filter(pk=cur_order).update(comment=comment)
        if user=='Гость':
            return reverse_lazy('home_page')
        else:
            return reverse_lazy('CRUDL_profiles:detail', kwargs={'pk':user.prof_user.pk})

    def get_success_message(self, cleaned_data):
        return f"{self.object}  - оформлен. Ожидайте звонка нашего специалиста."

class OrderUpdate(LoginRequiredMixin,UpdateView):
    model=Order
    template_name='order/o_update.html'
    fields=('contact_phone','status','comment',)

    def get_object(self, queryset=None):
        obj=super().get_object(queryset=queryset)
        global cur_comment
        cur_comment=obj.comment
        # order=Order.objects.get(pk=cur_order)
        # print('get_obj_comen',order.comment)
        return obj

    def get_success_url(self):

        #пример нотификации если заказ офоромлен
        # notify_managers(self.request.user, self.object)
        cdt=datetime.now()
        cdt=datetime.strftime(cdt,'%d.%m.%Y, %H:%M')
        user=self.request.user
        cur_order=self.object.pk
        order=Order.objects.get(pk=cur_order)
        print(order.comment)
        comment=cur_comment+'\n'+str(cdt)+' '+str(user)+':\n'+str(order.comment)
        if order.status==True:
            print('order.status==True / Canseled order')
            order=Order.objects.filter(pk=cur_order).update(status2='Отменен',comment={self.request.user:cdt})
        order=Order.objects.filter(pk=cur_order).update(comment=comment)
        prof_user=Profile.objects.get(username=user)
        return reverse_lazy("CRUDL_profiles:detail", kwargs={'pk':prof_user.pk})
