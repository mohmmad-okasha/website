# Generated by Django 4.1.6 on 2023-05-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_remove_subjects_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='timestamp',
            field=models.DateTimeField(blank=True),
            preserve_default=False,
        ),
    ]