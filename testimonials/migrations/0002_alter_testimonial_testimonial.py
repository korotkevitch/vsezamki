# Generated by Django 3.2.10 on 2022-01-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.CharField(blank=True, max_length=200, verbose_name='Отзыв'),
        ),
    ]