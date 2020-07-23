from django.db import models
from cart.models import Cart

# Create your models here.

class Order(models.Model):
    cart=models.OneToOneField(
        Cart,
        on_delete=models.PROTECT,
    )
    status=models.BooleanField(
        verbose_name="Отменить заказ",
        default=False
    )
    status2 = models.CharField(
        verbose_name='Статус заказа',
        choices=(('В обработке', 'В обработке'),('Доставка', 'Доставка'), ('Отменен', 'Отменен'),('Выполнен', 'Выполнен')),
        max_length= 100,
        default = 'В обработке',
    )

    delivery_address=models.TextField(
        verbose_name="Адрес доставки",
    )
    contact_phone=models.CharField(
        verbose_name="Контактный номер",
        max_length=15
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
    comment=models.TextField(
        verbose_name="Комментарий к заказу",
        blank=True,
        null=True
    )
    def __str__(self):
        return f"Order #{self.pk}"