# Generated by Django 3.2.10 on 2022-01-06 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_auto_20220106_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicedetailarticle',
            old_name='name',
            new_name='service',
        ),
    ]
