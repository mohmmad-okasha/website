# Generated by Django 4.1.6 on 2023-05-30 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_remove_links_created_at_remove_links_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 5, 30, 5, 55, 36, 564255, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='links',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 5, 30, 5, 55, 40, 645263, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjects',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]