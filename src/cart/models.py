from django.db import models
from django.contrib.auth.models import User
from books.models import Books

# Create your models here.
class Cart(models.Model):
    #пользователь корзины
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="carts",
    )
    # Дата создание корзины
    create=models.DateField(
        verbose_name="Дата внесения в каталог",
        auto_now=False,
        auto_now_add=True
    )
    # Дата изменения в корзине
    update=models.DateField( 
        verbose_name="Дата последнего изменения",
        auto_now=True,
        auto_now_add=False
    )
    
    def __str__(self):
        return f'Cart #{self.pk}'

class BookInCart(models.Model):
    cart=models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books'
    )
    books=models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name="books_in_cart"
    )

    qantity=models.IntegerField(
        verbose_name='Кол-во',
        default=1
    )

    def __str__(self):
        return f"Book #{self.books.pk} in cart #{self.cart.pk},qantity {self.qantity}"
    class Meta:
        unique_together=(('cart','books'),)
    
