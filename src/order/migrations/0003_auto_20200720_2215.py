# Generated by Django 3.0.7 on 2020-07-20 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200720_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Выполнен(да/нет)'),
        ),
    ]