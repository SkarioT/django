from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from .models import BookInCart,Cart
# Create your views here.

class AddBookToCart(UpdateView):
    models=BookInCart
    template_name='cart/add.html'
    fields=('qantity',)

    def get_object(self, queryset=None):
        obj,create = self.models.objects.get_or_create(
            cart={},
            books={},
            defaults={}
        )
        return obj