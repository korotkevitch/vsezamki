# Generated by Django 3.2.10 on 2022-01-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_remove_servicedetail_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetail',
            name='slug',
            field=models.SlugField(default='', max_length=80, unique=True),
        ),
    ]
