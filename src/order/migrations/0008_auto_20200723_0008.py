# Generated by Django 3.0.7 on 2020-07-22 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200723_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status2',
            field=models.CharField(choices=[('В обработке', 'В обработке'), ('Доставка', 'Доставка'), ('3', 'Отменен'), ('4', 'Закрыт')], default='Открыт', max_length=100, verbose_name='Статус заказа'),
        ),
    ]
