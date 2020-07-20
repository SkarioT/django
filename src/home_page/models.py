from django.db import models

# Create your models here.

class CourseData(models.Model):
    create=models.DateField(
        verbose_name="Текущая дата",
    )
    usd=models.FloatField(
        verbose_name='USD',
        blank=True,
        null=True
    )
    eur=models.FloatField(
        verbose_name='EUR',
        blank=True,
        null=True
    )
    rub=models.FloatField(
        verbose_name='RUB',
        blank=True,
        null=True
    )