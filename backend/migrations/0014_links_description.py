# Generated by Django 4.1.6 on 2023-05-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_rename_subject_name_links_subject_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='description',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
