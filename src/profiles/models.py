from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


from django.dispatch import receiver

User= get_user_model()

class Profile(models.Model):
    user=models.OneToOneField(
        User,
        related_name='prof_user',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    username=models.CharField(
        verbose_name="Имя пользователя",
        max_length=100,
        default=''
    )
    phone=models.CharField(
        verbose_name="Телефон",
        max_length=15,
        null=True,
        blank=True,
        default="375290000000"
    )
#     home_address=models.OneToOneField(
#         'ProfileAddress',
#         on_delete=models.CASCADE,
#         verbose_name="Домашний адрес",
#         default=1,
#         null=True,
#         blank=True,
#     )
#     def __str__(self):
#         return f"{self.user}"

# class ProfileAddress(models.Model):
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=128,
        blank=True)
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=128,
        blank=True)
    address_1 = models.CharField(
        verbose_name="Адресс 1",
        max_length=128,
        blank=True)
    address_2 = models.CharField(
        verbose_name="Адресс 2",
        max_length=128,
        blank=True)
    city = models.CharField(
        verbose_name="Город",
        max_length=64,
        default="Минск",
        blank=True
        )
    county = models.CharField(
        verbose_name="Страна",
        max_length=64,
        default="Беларусь",
        blank=True
        )
    zip_code = models.CharField(
        verbose_name="Почтовый индекс",
        max_length=5,
        default="23555",
        blank=True
        )

    def __str__(self):
        return f"{self.user}, {self.county},{self.city},{self.address_1},{self.address_2},{self.zip_code}"
# fields=('username','password','first_name','last_name','email')

#функция сигнал, при кком либо изменние в User, менят для User.last_name имя на "upd_lastname_from_signal"
# def test_singal(sender,instance, **kwargs):
#     instance.last_name="upd_lastname_from_signal"
#испольем pre_save,т.к. при созднии post_save требовлось бы выполнение instance.save(),что в свою очередь запукло рекурсию. т.е. сохроняем, 
# стрбывет сигнал на измениние, изменят, сохроняем, вызывает сигнал и так пока не страшимся.
#                 фун.обрботик, откуда сигнал
# pre_save.connect(test_singal,sender=User)


