# Generated by Django 3.0.7 on 2020-07-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles-pic', verbose_name='Фото пользователя'),
        ),
    ]
