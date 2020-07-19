from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from profiles.models import Profile
from books.models import Books
from cart.models import Cart,BookInCart
from .models import Order
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# Create your views here.

class CreateOrder(UpdateView):
    model=Order
    context_object_name='order'
    template_name="order/create.html"
    fields=('delivery_address','contact_phone',)
    success_url=reverse_lazy("cart:my")

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
        print("obj",obj.pk)
        return obj

    def get_success_url(self):
        url=super().get_success_url()
        #пример нотификации если заказ офоромлен
        # notify_managers(self.request.user, self.object)
        del(self.request.session['cart_pk'])
        return url

