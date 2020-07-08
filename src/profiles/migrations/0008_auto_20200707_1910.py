# Generated by Django 3.0.7 on 2020-07-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_1',
            field=models.CharField(blank=True, max_length=128, verbose_name='Адресс 1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_2',
            field=models.CharField(blank=True, max_length=128, verbose_name='Адресс 2'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Фамилия'),
        ),
    ]