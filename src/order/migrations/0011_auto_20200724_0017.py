# Generated by Django 3.0.7 on 2020-07-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20200723_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Отменить заказ'),
        ),
    ]
