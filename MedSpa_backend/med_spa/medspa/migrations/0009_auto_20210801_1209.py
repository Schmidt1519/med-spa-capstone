# Generated by Django 3.1.8 on 2021-08-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medspa', '0008_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=800),
        ),
    ]