  
from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from .models import BookInCart,Cart
from profiles.models import Profile
from books.models import Books
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Create your views here.



class AddBookToCart(UpdateView):
    models=BookInCart
    template_name='cart/add.html'
    fields=('qantity',)
    success_url =reverse_lazy('cart:my')

    def get_object(self, queryset=None):
        #из запросы берём book_pk
        book_pk=self.request.GET.get('book_pk')
        #получаем объект кники по pk=book_pk
        books=Books.objects.get(pk=book_pk)

        #получаем текущего юзера
        user=self.request.user 
        if user.is_anonymous:
            user=None
        #получаем cart_pk из сессии(из куков),если в куках пусто - отдаём None
        cart_pk=self.request.session.get('cart_pk',None) 
        if cart_pk is not None:
            cart_pk=int(cart_pk)
        #производим поиск на освани данных из куков, если в куках нашло - получаем корзину,
        #  не нашло ( вернуло 0, а пк=0 быть не может)  - создаём новую корзину
        cart,create = Cart.objects.get_or_create(
            pk=cart_pk,
            user=user,
            defaults={}
        )
        if create:
            self.request.session['cart_pk']=cart.pk

        obj,create = self.models.objects.get_or_create(
            cart=cart,
            books=books,
            defaults={}
        )
        return obj

    def form_valid(self, form):
        book_pk = self.request.GET.get('book_pk')
        book = Books.objects.get(pk=book_pk)
        qantity = self.request.POST['qantity']
        if int(qantity) <= book.count_book:
            form.save()
            return super(AddBookToCart, self).form_valid(form)
        else:
            messages.error(self.request, f'Запрос привышает допустимое кол-во. Максимальное кол-во книг - { book.count_book }') 
            return render(self.request, 'cart/add.html', {'form': form})

        
class CartDetail(DetailView):
    model=Cart
    template_name='cart/detail.html'
    
    def get_object(self, queryset=None):
        user=self.request.user
        if user.is_anonymous:
            user=None
        cart_pk=self.request.session.get('cart_pk',None)
        print('cart_pk:',cart_pk)
        cart,create = Cart.objects.get_or_create(
            pk=cart_pk,
            user=user,
            defaults={}
        )
        if create:
            self.request.session['cart_pk']=cart.pk

        return cart




class BookInCartDelete(DeleteView):
    model=BookInCart
    success_url =reverse_lazy('cart:my')
    template_name='cart/delete.html'

