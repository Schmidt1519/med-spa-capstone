# Generated by Django 3.1.8 on 2021-07-29 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medspa', '0003_auto_20210729_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]