# Generated by Django 3.2.10 on 2022-01-06 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_auto_20220106_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetailarticle',
            name='service',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='service.servicedetail'),
        ),
    ]
