# Generated by Django 3.2.4 on 2021-06-06 11:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 11, 12, 41, 585760, tzinfo=utc), verbose_name='Date published'),
        ),
    ]
