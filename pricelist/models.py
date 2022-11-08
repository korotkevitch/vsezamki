from django.db import models
from service.models import ServiceDetail


class Price(models.Model):
    service = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE, verbose_name='Услуга')
    item_1 = models.CharField('Цена 1', max_length=150, blank=True)
    item_2 = models.CharField('Цена 2', max_length=150, blank=True)
    item_3 = models.CharField('Цена 3', max_length=150, blank=True)
    item_4 = models.CharField('Цена 4', max_length=150, blank=True)
    item_5 = models.CharField('Цена 5', max_length=150, blank=True)
    item_6 = models.CharField('Цена 6', max_length=150, blank=True)
    item_7 = models.CharField('Цена 7', max_length=150, blank=True)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return str(self.service)
