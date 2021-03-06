# Generated by Django 3.2 on 2022-03-07 19:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20220307_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
