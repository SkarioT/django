# Generated by Django 3.0.7 on 2020-07-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200716_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.ManyToManyField(related_name='publisher_books', to='books.Publisher', verbose_name='Издательство'),
        ),
    ]
