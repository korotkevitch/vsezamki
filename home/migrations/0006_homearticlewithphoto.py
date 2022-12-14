# Generated by Django 3.2.10 on 2022-01-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homearticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeArticleWithPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Название статьи')),
                ('text', models.CharField(blank=True, max_length=10000, verbose_name='Текст статьи')),
            ],
            options={
                'verbose_name': 'Статья с фото',
                'verbose_name_plural': 'Статьи с фото',
            },
        ),
    ]
