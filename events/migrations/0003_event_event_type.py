# Generated by Django 3.2 on 2022-02-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(blank=True, choices=[('WEDDING', 'Wedding'), ('CHRISTENING', 'Christening'), ('OTHER', 'Other')], max_length=20),
        ),
    ]