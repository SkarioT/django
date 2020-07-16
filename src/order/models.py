from django.db import models
from cart.models import Cart

# Create your models here.

class Order(models.Model):
    cart=models.OneToOneField(
        Cart,
        on_delete=models.PROTECT
    )
    status=models.BooleanField(
        verbose_name="Статус заказа",
        default=False
    )

    delivery_address=models.TextField(
        verbose_name="Адрес доставки",
    )
    contact_phone=models.CharField(
        verbose_name="Контактный номер",
        max_length=50
    )
    create=models.DateField(
        verbose_name="Дата cоздания",
        auto_now=False,
        auto_now_add=True
    )
    update=models.DateField(
        verbose_name="Дата последнего изменения",
        auto_now=True,
        auto_now_add=False
    )