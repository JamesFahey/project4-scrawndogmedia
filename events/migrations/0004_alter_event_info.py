# Generated by Django 3.2 on 2022-02-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='info',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
