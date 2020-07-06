from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


from django.dispatch import receiver

User= get_user_model()

class Profile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    image=models.ImageField(
        verbose_name="Фото пользователя",
        upload_to="profiles-pic",
        null=True,
        blank=True,
    )

    phone=models.CharField(
        verbose_name="Телефон",
        max_length=15,
        null=True,
        blank=True,
        default="375290000000"
    )
    def __str__(self):
        return f"{self.user}"

#функция сигнал, при кком либо изменние в User, менят для User.last_name имя на "upd_lastname_from_signal"
# def test_singal(sender,instance, **kwargs):
#     instance.last_name="upd_lastname_from_signal"
#испольем pre_save,т.к. при созднии post_save требовлось бы выполнение instance.save(),что в свою очередь запукло рекурсию. т.е. сохроняем, 
# стрбывет сигнал на измениние, изменят, сохроняем, вызывает сигнал и так пока не страшимся.
#                 фун.обрботик, откуда сигнал
# pre_save.connect(test_singal,sender=User)


