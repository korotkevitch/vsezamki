# Generated by Django 3.2.10 on 2022-01-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, verbose_name='Title страницы')),
                ('image', models.FileField(blank=True, upload_to='', verbose_name='Главное фото')),
            ],
            options={
                'verbose_name': 'Верхняя часть с фото',
                'verbose_name_plural': 'Верхняя часть с фото',
            },
        ),
    ]