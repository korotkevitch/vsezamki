# Generated by Django 3.2.10 on 2022-01-13 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0024_remove_servicedetail_text_on_image'),
        ('pricelist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicedetail', verbose_name='Услуга'),
        ),
    ]
