from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from app.models import SlugModel

# Create your models here.


class House(SlugModel):

    class Meta:
        verbose_name_plural = 'houses'
        verbose_name = 'house'

    name = models.CharField('Nombre', max_length=50)
    address = models.CharField('Dirección', max_length=100)
    surface = models.DecimalField('m2 de superficie',
                                  max_digits=7,
                                  decimal_places=2,
                                  validators=[MinValueValidator(Decimal('0.01'))])
    contact_email = models.EmailField('Email de contacto')

    def __str__(self):
        return self.name
