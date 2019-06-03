from django.db import models
from shop.models import Product
from cupons.models import Cupon
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

class Emp_project(models.Model):
    Status = models.CharField(verbose_name='Имя', max_length=50)
    Priority = models.CharField(verbose_name='Имя', max_length=50)
# Create your models here.
