# Generated by Django 3.1.8 on 2021-07-29 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medspa', '0006_auto_20210729_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
