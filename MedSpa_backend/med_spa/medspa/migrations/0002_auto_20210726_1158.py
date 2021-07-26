# Generated by Django 3.1.8 on 2021-07-26 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medspa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='service_id',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='appointment_id',
            new_name='appointment',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='service_id',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='user_id',
            new_name='user',
        ),
    ]
