# Generated by Django 3.2 on 2022-02-24 20:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_booking_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='booking',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 2, 24, 20, 5, 16, 481114, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('event_type', models.CharField(blank=True, choices=[('WEDDING', 'Wedding'), ('CHRISTENING', 'Christening'), ('OTHER', 'Other')], max_length=30, null=True)),
                ('event_date', models.DateField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('info', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Requested'), (1, 'Confirmed')], default=0, null=True)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edit', to='events.booking')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
