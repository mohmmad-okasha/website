# Generated by Django 4.1.6 on 2023-05-30 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_remove_links_created_at_remove_links_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
