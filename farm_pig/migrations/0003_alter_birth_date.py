# Generated by Django 4.0.5 on 2022-06-30 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_pig', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birth',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 30, 8, 48, 1, 762468)),
        ),
    ]
