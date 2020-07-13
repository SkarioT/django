from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from .models import BookInCart,Cart
from books.models import Books
from profiles.models import Profile
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AddBookToCart(LoginRequiredMixin,UpdateView):
    models=BookInCart
    template_name='cart/add.html'
    fields=('qantity',)
    success_url =reverse_lazy('home_page')

    def get_object(self, queryset=None):
        #из запросы берём book_pk
        book_pk=self.request.GET.get('book_pk')
        #получаем объект кники по pk=book_pk
        books=Books.objects.get(pk=book_pk)

        #получаем текущего юзера
        user=self.request.user 

        #получаем cart_pk из сессии(из куков),если в куках пусто - отдаём None
        cart_pk=self.request.session.get('cart_pk',0)

        #производим поиск на освани данных из куков, если в куках нашло - получаем корзину,
        #  не нашло ( вернуло 0, а пк=0 быть не может)  - создаём новую корзину
        if user.is_anonymous:
            user=None
        cart,create = Cart.objects.get_or_create(
            pk=int(cart_pk),
            defaults={
                "user": user,
            }
        )
        if create:
            cart_pk=self.request.session['cart_pk']=cart.pk

        obj,create = self.models.objects.get_or_create(
            cart=cart,
            books=books,
            defaults={}
        )
        return obj

    def get_context_data(self, **kwargs):
        #подкидуываю в контектс для каждого обработчика в контект Profile user pk
        c= super().get_context_data(**kwargs)
        try:
            user=self.request.user
            prof_user=Profile.objects.get(username=user)
            print(user)
            print('prof_user.pk',prof_user.pk)
            c['prof_user']=prof_user.pk
        except Profile.DoesNotExist:
            prof_user=None
        return c

class CartDetail(LoginRequiredMixin,ListView):
    models=Cart
    template_name='cart/list.html'
    
    def get_object(self, queryset=None):
        #из запросы берём book_pk
        book_pk=self.request.GET.get('book_pk')
        #получаем объект кники по pk=book_pk
        books=Books.objects.get(pk=book_pk)

        #получаем текущего юзера
        user=self.request.user 

        #получаем cart_pk из сессии(из куков),если в куках пусто - отдаём None
        cart_pk=self.request.session.get('cart_pk',0)

        #производим поиск на освани данных из куков, если в куках нашло - получаем корзину,
        #  не нашло ( вернуло 0, а пк=0 быть не может)  - создаём новую корзину
        if user.is_anonymous:
            user=None
        cart,create = Cart.objects.get_or_create(
            pk=int(cart_pk),
            defaults={
                "user": user,
            }
        )
        if create:
            cart_pk=self.request.session['cart_pk']=cart.pk

        obj,create = self.models.objects.get_or_create(
            cart=cart,
            books=books,
            defaults={}
        )
        return obj