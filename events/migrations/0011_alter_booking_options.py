# Generated by Django 3.2 on 2022-02-24 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_edit_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['event_date']},
        ),
    ]
