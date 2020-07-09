from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from .models import BookInCart,Cart
from books.models import Books
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
        cart_pk=self.request.session.get('cart_pk',None)


        #производим поиск на освани данных из куков, если в куках нашло - получаем корзину,
        #  не нашло ( вернуло 0, а пк=0 быть не может)  - создаём новую корзину
        cart,create = Cart.objects.get_or_create(
            pk=cart_pk,
            user=user,
            defaults={}
        )
        if create:
            cart_pk=self.request.session['cart_pk']=cart.pk

        obj,create = self.models.objects.get_or_create(
            cart=cart,
            books=books,
            defaults={}
        )
        return obj