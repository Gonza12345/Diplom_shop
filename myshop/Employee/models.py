from django.db import models
from shop.models import Product
from cupons.models import Cupon
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


class Employee(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    Middle_name = models.CharField(verbose_name='Фамилия', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    Local_phone_num = models.IntegerField(default=0, max_length=12)
    City_phone_num = models.IntegerField(default=0, max_length=12)
    Position = models.CharField(verbose_name='Фамилия', max_length=50)


    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)




