# Generated by Django 3.2.10 on 2022-01-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220104_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=55, verbose_name='Заголовок')),
                ('intro', models.CharField(blank=True, max_length=200, verbose_name='Текст под заголовком')),
                ('image', models.FileField(blank=True, upload_to='', verbose_name='Изображение для видео')),
                ('link', models.CharField(blank=True, max_length=200, verbose_name='Ссылка на видео')),
                ('subtitle_1', models.CharField(blank=True, max_length=15, verbose_name='Подзаголовок 1')),
                ('text_1', models.CharField(blank=True, max_length=220, verbose_name='Текст 1')),
                ('subtitle_2', models.CharField(blank=True, max_length=15, verbose_name='Подзаголовок 2')),
                ('text_2', models.CharField(blank=True, max_length=220, verbose_name='Текст 2')),
                ('subtitle_3', models.CharField(blank=True, max_length=15, verbose_name='Подзаголовок 3')),
                ('text_3', models.CharField(blank=True, max_length=220, verbose_name='Текст 3')),
                ('label', models.CharField(blank=True, max_length=20, verbose_name='Ярлык на картинке')),
            ],
            options={
                'verbose_name': 'Блок с видео',
                'verbose_name_plural': 'Блок с видео',
            },
        ),
    ]
