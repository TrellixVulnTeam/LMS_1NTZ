# Generated by Django 3.0.4 on 2020-03-29 04:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200328_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 29, 10, 16, 0, 514701)),
        ),
    ]
