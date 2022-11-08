from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


class ServiceDetail(models.Model):
    service = models.CharField('Название услуги', max_length=20, blank=True)
    image_little = models.FileField('Малое фото', blank=True)
    text_under_image = models.CharField('Текст под фото на "Services"', max_length=200, blank=True)
    image_big = models.FileField('Большое фото', blank=True)
    slug = models.SlugField(max_length=80, unique=True)

    def get_url(self):
        return reverse('service_details', args=[self.slug])

    def image_little_preview(self):
        if self.image_little:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image_little.url)
        else:
            return 'No Image Found'

    image_little_preview.short_description = 'Фото маленькое'

    def image_big_preview(self):
        if self.image_big:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image_big.url)
        else:
            return 'No Image Found'

    image_big_preview.short_description = 'Фото большое'

    class Meta:
        verbose_name = '  Услуга'
        verbose_name_plural = '   Список услуг'

    def __str__(self):
        return self.service


class ServiceListArticle(models.Model):
    title = models.CharField('Название статьи', max_length=100, blank=True)
    text = models.CharField('Текст статьи', max_length=10000, blank=True)
    is_activated = models.BooleanField(default=True)

    class Meta:
        verbose_name = ' Статья к разделу "Услуги"'
        verbose_name_plural = ' Статьи к разделу "Услуги"'

    def __str__(self):
        return self.title


class ServiceDetailArticle(models.Model):
    service = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE, default="", verbose_name='Услуга')
    title = models.CharField('Название статьи', max_length=100, blank=True)
    text = models.CharField('Текст статьи', max_length=10000, blank=True)
    is_activated = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Статья к отдельной услуге'
        verbose_name_plural = 'Статьи к отдельной услуге'

    def __str__(self):
        return self.title




