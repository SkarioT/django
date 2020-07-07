# Generated by Django 3.0.7 on 2020-07-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, default='example@example.com', max_length=40, null=True, verbose_name='Фамилия'),
        ),
    ]
