# Generated by Django 3.0.4 on 2020-04-07 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200407_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 23, 5, 50, 154558)),
        ),
    ]
