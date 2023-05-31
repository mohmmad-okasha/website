# Generated by Django 4.1.5 on 2023-05-26 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_remove_links_subjects_id_remove_subjects_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='subject_id',
        ),
        migrations.AddField(
            model_name='links',
            name='subject_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend.subjects'),
            preserve_default=False,
        ),
    ]