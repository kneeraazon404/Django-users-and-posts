# Generated by Django 2.2.2 on 2019-07-05 16:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.URLField(default=datetime.datetime(2019, 7, 5, 16, 28, 54, 346822, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
