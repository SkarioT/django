# Generated by Django 3.0.7 on 2020-06-16 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('lastn_name', models.CharField(max_length=50, verbose_name='Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Binging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип переплёта')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название Жанра')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание Жанра')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя книги')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Цена')),
                ('publishing_year', models.IntegerField(default=2020, verbose_name='Год издания')),
                ('number_page', models.IntegerField(default=100, verbose_name='Кол-во страниц')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие книги')),
                ('author', models.ManyToManyField(to='books.Author', verbose_name='Автор')),
                ('binging', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='books.Binging', verbose_name='Переплёт')),
                ('genre', models.ManyToManyField(to='books.Genre', verbose_name='Жанр')),
            ],
        ),
    ]