# Generated by Django 3.1.7 on 2021-03-24 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todos'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 3, 24, 8, 10, 26, 268699, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
