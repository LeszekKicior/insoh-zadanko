# Generated by Django 2.0.5 on 2018-05-12 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclemanager', '0005_auto_20180512_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battery',
            name='battery_number',
        ),
    ]
