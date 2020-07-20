# Generated by Django 3.0.7 on 2020-07-17 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200716_1727'),
        ('order', '0002_auto_20200717_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cart.Cart'),
        ),
    ]