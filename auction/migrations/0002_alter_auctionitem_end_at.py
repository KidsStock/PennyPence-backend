# Generated by Django 3.2.13 on 2023-02-19 05:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='end_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 26, 5, 38, 38, 824433, tzinfo=utc)),
        ),
    ]
