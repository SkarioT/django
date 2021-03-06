from django.db import models
import datetime
# Create your models here.
class Genre(models.Model):
    #id/pk
    name = models.CharField(
        verbose_name ="Название Жанра",
        max_length=30
        ) # столбец name тип данных CharField
    description = models.TextField(
        verbose_name="Описание Жанра",
        null=True,
        blank=True
    )
    update=models.DateField(
        verbose_name="Дата обновления",
        auto_now=True,
        auto_now_add=False
    )
    create=models.DateField(
        verbose_name="Дата ооздания",
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
    

# class Book(models.Model):
#     name = models.CharField(
#         verbose_name ="Название книги",
#         max_length=200
#     )
#     description = models.TextField(
#         verbose_name="Описание книги",
#         null=True,
#         blank=True
#     )
#     genre=models.ForeignKey(
#         Genre,
#         on_delete=models.PROTECT,
#         verbose_name="Жанр Книги"
#     )
#     created=models.DateField(
#         verbose_name="Дата создания",
#         auto_now=True,
#         auto_now_add=False
#     )
#     update=models.DateField(
#         verbose_name="Дата обновления",
#         auto_now=False,
#         auto_now_add=True
#     )

#     def __str__(self):
#         return self.name    
#      # столбец name тип данных CharField