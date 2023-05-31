# Generated by Django 4.1.5 on 2023-05-26 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_links_subjects_delete_accounts_delete_customers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='subjects_id',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='name',
        ),
        migrations.AddField(
            model_name='links',
            name='subject_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='name', to='backend.subjects'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjects',
            name='subject_name',
            field=models.CharField(default=' ', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]