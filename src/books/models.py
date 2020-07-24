from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth import get_user_model

User= get_user_model()
# Create your models here.
class Books(models.Model):
    #1)Название книги
    name=models.CharField(
        verbose_name="Имя книги",
        max_length=100
    )
    description = models.TextField(
        verbose_name='Описание книги',
        null=True,
        blank=True
    )
    #2)Фото обложки
    picture=models.ImageField(
        verbose_name="Фото обложки",
        upload_to="books-pic",
        null=True,
        blank=True,
        default="books-pic/default.jpg"
    )

    # 3) Цена
    price=models.DecimalField(
        verbose_name="Цена",
        max_digits=5,
        decimal_places=2,
        default=00.00
    )
    # 4)Автор книги
    author=models.ManyToManyField(
        'Author',
        verbose_name="Автор",
        related_name="books_author"
    )
    # 5)Серия
    series=models.ManyToManyField(
        'Series',
        verbose_name="Серия",
        related_name="series_books",
        blank=True,
    )

    # 6) Жанр книги
    genre=models.ManyToManyField(
        'Genre',
        verbose_name="Жанр",
        related_name="genre_books"
    )

    # 7)Год издания
    publishing_year=models.PositiveSmallIntegerField (
        verbose_name="Год издания",
        default=2020
    )

    # 8)Кол-во страниц
    count_page=models.IntegerField(
        verbose_name="Кол-во страниц",
        default=100
    )

    # 9) Переплёт
    binging=models.ForeignKey(
        'Binging',
        verbose_name="Переплёт",
        on_delete=models.PROTECT,
        default=1
    )
    # 10)Формат
    format_book=models.CharField(
        verbose_name="Формат",
        default="99x99",
        max_length=15
    )
    # 11)ISBN
    isbn=models.CharField(
        verbose_name="ISBN",
        default="999-1-88877-6",
        max_length=15
    )
    # 12) Вес(гр)
    weight=models.PositiveSmallIntegerField(
        verbose_name="Вес(гр.)",
        default="100"
    )
    # 13) возрастные ограничения
    age_limit=models.CharField(
        verbose_name="Ограничение по возрасту",
        default="6+",
        max_length=3
    )
    # 14)Издательство
    publisher=models.ManyToManyField(
        'Publisher',
        verbose_name="Издательство",
        related_name="publisher_books"
    )
    
    # 15) Кол-во книг в наличии
    count_book=models.IntegerField(
        verbose_name="Ко-во книг в наличии",
        default=100
    )
    # 16) наличие/доступен ли для заказа
    availability=models.BooleanField(
        verbose_name="Наличие книги",
        default=True
    )
    # 17) Рейтинг
    rating=models.FloatField(
        verbose_name="Рейтинг",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=9
    )
    # 18)Дата внесения в каталог"
    created=models.DateField(
        verbose_name="Дата внесения в каталог",
        auto_now=False,
        auto_now_add=True
    )
    # 19)"Дата последнего изменения"
    updated=models.DateField(
        verbose_name="Дата последнего изменения",
        auto_now=True,
        auto_now_add=False
    )

    user=models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=2
    )

    def __str__(self):
        return f"{self.name}"

class Author(models.Model):
    first_name=models.CharField(
        verbose_name="Имя",
        max_length=50
    )
    last_name=models.CharField(
        verbose_name="Фамилия",
        max_length=50
    )
    description = models.TextField(
        verbose_name="Информация об атворе",
        null=True,
        blank=True,
        default='Информация об авторескоро будет добавлена на сайт. Сделать ее более полной и интересной помогут объективные отзывы тех, кто хорошо знаком с творчеством и фактами биографии данного автора. Оставляйте свои комментарии, делитесь впечатлениями и вступайте в дискуссии — это поможет другим сделать выбор.'
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):

    name = models.CharField(
        verbose_name ="Название Жанра",
        max_length=30
        ) 
    description = models.TextField(
        verbose_name="Описание Жанра",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"
        
class Binging(models.Model):
    name = models.CharField(
        verbose_name ="Тип переплёта",
        max_length=30
        )     
    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(
        verbose_name ="Серия книг",
        max_length=50
        )     
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(
        verbose_name ="Издатель",
        max_length=50
        )     
    def __str__(self):
        return self.name
