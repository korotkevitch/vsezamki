from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from django.utils import timezone


class Contact(models.Model):
    phone = models.CharField('Телефон', max_length=50, blank=True)
    viber = PhoneNumberField('Вайбер', null=False, blank=False, unique=True)
    email = models.EmailField('Email', max_length=50, blank=True)

    def phone_link(self):
        return PhoneNumber.from_string(phone_number=self.phone, region='RU').as_e164

    phone_link.short_description = 'Телефон для ссылки'

    def viber_link(self):
        number = str(self.viber)
        return number.replace('+', '')

    viber_link.short_description = 'Вайбер без +'

    class Meta:
        verbose_name = '       Контактные данные'
        verbose_name_plural = '       Контактные данные'

    def __str__(self):
        return "Телефоны"


class ContactForm(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True)
    email = models.EmailField('Емейл', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    message = models.TextField('Сообщение', max_length=500, blank=True)

    class Meta:
        verbose_name = 'Сообщение, заказ'
        verbose_name_plural = 'Сообщения, заказы'

    def __str__(self):
        return self.name