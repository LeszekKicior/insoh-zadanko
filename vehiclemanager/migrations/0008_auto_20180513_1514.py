# Generated by Django 2.0.5 on 2018-05-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclemanager', '0007_battery_battery_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='battery',
            name='battery_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='battery',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
