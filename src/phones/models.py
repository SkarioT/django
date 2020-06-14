from django.db import models

# Create your models here.
class Phone(models.Model):

    number = models.CharField(
        verbose_name="Phone",
        max_length=20
    )
    #contact - User
    #type -> Catalog
    def __str__(self):
        return self.number