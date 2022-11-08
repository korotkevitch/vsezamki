from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from datetime import datetime
from django.utils import timezone
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
from service.models import ServiceDetail


class ArticleList(models.Model):
    title = models.CharField('Заголовок раздела', max_length=100, blank=True)
    text = models.CharField('Описание раздела', max_length=10000, blank=True)
    is_activated = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Раздел "Статьи"'
        verbose_name_plural = 'Раздел "Статьи"'

    def __str__(self):
        return self.title


class ArticleDetail(models.Model):
    service = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE, default="", verbose_name='Услуга')
    title = models.CharField('Название статьи', max_length=100, blank=True)
    description = models.CharField('Краткое описание', max_length=150, blank=True)
    image = models.FileField('Изображение для статьи', blank=True)
    text = models.CharField('Текст статьи', max_length=10000, blank=True)
    created_date = models.DateField('Дата создания', default=timezone.now)
    is_activated = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True)

    def get_url(self):
        return reverse('article_details', kwargs={'service_slug': self.service.slug, 'article_slug': self.slug })

    def mon(self):
        return self.created_date.strftime('%B')

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Статья по теме'
        verbose_name_plural = 'Статьи по темам'

    def __str__(self):
        return self.title