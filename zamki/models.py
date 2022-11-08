from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils import timezone


# class Article(models.Model):
#     page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Страница')
#     title = models.CharField('Название статьи', max_length=100, blank=True)
#     text = models.CharField('Текст статьи', max_length=10000, blank=True)
#     image = models.FileField('Изображение для статьи', blank=True)
#     slug = models.SlugField(max_length=100, unique=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     is_activated = models.BooleanField(default=True)
#
#     def image_preview(self):
#         if self.image:
#             return mark_safe('<img src="%s" style="width:80px; height:100px;" />' % self.image.url)
#         else:
#             return 'No Image Found'
#
#     image_preview.short_description = 'Фото'
#
#     class Meta:
#         verbose_name = '   Статья'
#         verbose_name_plural = '   Статьи'
#
#     def __str__(self):
#         return self.title
