# Generated by Django 3.0.7 on 2020-07-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20200707_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=100, verbose_name='Имя пользователя'),
        ),
    ]
