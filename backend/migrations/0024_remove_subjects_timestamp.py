# Generated by Django 4.1.6 on 2023-05-30 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_alter_subjects_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='timestamp',
        ),
    ]
