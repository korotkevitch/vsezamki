from django.db import models


class Testimonial(models.Model):
    name = models.CharField('Автор отзыва', max_length=50, blank=True)
    testimonial = models.CharField('Отзыв', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
