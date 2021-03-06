# Generated by Django 3.0.7 on 2020-07-20 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0010_auto_20200719_2041'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Дата внесения в каталог')),
                ('update', models.DateField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qantity', models.IntegerField(default=1, verbose_name='Кол-во')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_in_cart', to='books.Books')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='cart.Cart')),
            ],
            options={
                'unique_together': {('cart', 'books')},
            },
        ),
    ]
