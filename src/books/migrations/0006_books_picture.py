# Generated by Django 3.0.7 on 2020-06-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200617_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='books-pic', verbose_name='Фото обложки'),
        ),
    ]