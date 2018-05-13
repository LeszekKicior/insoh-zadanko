# Generated by Django 2.0.5 on 2018-05-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclemanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='battery',
            options={'verbose_name_plural': 'batteries'},
        ),
        migrations.AddField(
            model_name='vehicle',
            name='user_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
