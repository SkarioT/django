# Generated by Django 3.0.7 on 2020-07-20 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Статус заказа')),
                ('delivery_address', models.TextField(verbose_name='Адрес доставки')),
                ('contact_phone', models.CharField(max_length=15, verbose_name='Контактный номер')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Дата cоздания')),
                ('update', models.DateField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cart.Cart')),
            ],
        ),
    ]
