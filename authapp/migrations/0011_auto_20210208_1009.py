# Generated by Django 2.2.17 on 2021-02-08 07:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20210126_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 10, 7, 9, 3, 415613, tzinfo=utc)),
        ),
    ]
