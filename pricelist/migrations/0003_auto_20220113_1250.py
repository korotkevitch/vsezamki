# Generated by Django 3.2.10 on 2022-01-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricelist', '0002_alter_price_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
        migrations.RemoveField(
            model_name='price',
            name='item',
        ),
        migrations.AddField(
            model_name='price',
            name='item_1',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цена 1'),
        ),
        migrations.AddField(
            model_name='price',
            name='item_2',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цена 2'),
        ),
        migrations.AddField(
            model_name='price',
            name='item_3',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цена 3'),
        ),
        migrations.AddField(
            model_name='price',
            name='item_4',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цена 4'),
        ),
        migrations.AddField(
            model_name='price',
            name='item_5',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цена 5'),
        ),
        migrations.AddField(
            model_name='price',
            name='item_6',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цена 6'),
        ),
        migrations.AddField(
            model_name='price',
            name='item_7',
            field=models.CharField(blank=True, max_length=150, verbose_name='Цена 7'),
        ),
    ]