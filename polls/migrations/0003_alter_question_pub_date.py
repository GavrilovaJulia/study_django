# Generated by Django 3.2.4 on 2021-06-06 11:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 11, 20, 57, 147145, tzinfo=utc), verbose_name='Date published'),
        ),
    ]
