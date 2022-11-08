from django.db import models
from django.utils.safestring import mark_safe


class Head(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True)
    image = models.FileField('Главное фото', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото в шапке'

    class Meta:
        verbose_name = '       Верхняя часть с фото'
        verbose_name_plural ='       Верхняя часть с фото'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField('Название раздела', max_length=50, blank=True)
    text = models.CharField('Текст, до 200 зн.', max_length=200, blank=True)

    class Meta:
        verbose_name = '      Раздел "О компании"'
        verbose_name_plural = '      Раздел "О компании"'

    def __str__(self):
        return self.title


class Principle(models.Model):
    title = models.CharField('Заголовок', max_length=50, blank=True)
    text = models.CharField('Текст, до 120 зн.', max_length=120, blank=True)
    image = models.FileField('Картинка', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:50px; height:50px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Картинка'

    class Meta:
        verbose_name = '     Принцип работы'
        verbose_name_plural = '     Принципы работы'

    def __str__(self):
        return self.title


class VideoBlock(models.Model):
    title = models.CharField('Заголовок', max_length=55, blank=True)
    intro = models.CharField('Текст под заголовком', max_length=200, blank=True)
    image = models.FileField('Изображение для видео', blank=True)
    link = models.CharField('Ссылка на видео', max_length=200, blank=True)
    subtitle_1 = models.CharField('Подзаголовок 1', max_length=15, blank=True)
    text_1 = models.CharField('Текст 1', max_length=220, blank=True)
    subtitle_2 = models.CharField('Подзаголовок 2', max_length=15, blank=True)
    text_2 = models.CharField('Текст 2', max_length=220, blank=True)
    subtitle_3 = models.CharField('Подзаголовок 3', max_length=15, blank=True)
    text_3 = models.CharField('Текст 3', max_length=220, blank=True)
    label = models.CharField('Ярлык на картинке', max_length=20, blank=True)


    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = '    Блок с видео'
        verbose_name_plural = '    Блок с видео'

    def __str__(self):
        return self.title


class HomeArticleWithPhoto(models.Model):
    title = models.CharField('Название статьи', max_length=100, blank=True)
    text = models.CharField('Текст статьи', max_length=10000, blank=True)
    image = models.FileField('Изображение для статьи', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = '   Статья с фото'
        verbose_name_plural = '   Статьи с фото'

    def __str__(self):
        return self.title


class HomeArticle(models.Model):
    title = models.CharField('Название статьи', max_length=100, blank=True)
    text = models.CharField('Текст статьи', max_length=10000, blank=True)
    is_activated = models.BooleanField(default=True)


    class Meta:
        verbose_name = '  Статья без фото'
        verbose_name_plural = '  Статьи без фото'

    def __str__(self):
        return self.title