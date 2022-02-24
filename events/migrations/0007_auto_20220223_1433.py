# Generated by Django 3.2 on 2022-02-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20220223_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='event',
        ),
        migrations.AddField(
            model_name='booking',
            name='event_type',
            field=models.CharField(blank=True, choices=[('WEDDING', 'Wedding'), ('CHRISTENING', 'Christening'), ('OTHER', 'Other')], max_length=30, null=True),
        ),
    ]
