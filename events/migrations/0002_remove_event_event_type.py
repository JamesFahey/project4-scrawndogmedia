# Generated by Django 3.2 on 2022-02-16 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_type',
        ),
    ]
