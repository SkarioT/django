# Generated by Django 3.0.7 on 2020-07-22 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20200723_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status2',
            field=models.CharField(choices=[('1', 'В обработке'), ('Доставка', 'Доставка'), ('3', 'Отменен'), ('4', 'Закрыт')], default='Открыт', max_length=100, verbose_name='Статус заказа'),
        ),
    ]