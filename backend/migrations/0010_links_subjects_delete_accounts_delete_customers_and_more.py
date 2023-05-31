# Generated by Django 4.1.5 on 2023-05-25 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_rename_tree_accounts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Accounts',
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.DeleteModel(
            name='Dashboard_buttons',
        ),
        migrations.AddField(
            model_name='links',
            name='subjects_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.subjects'),
        ),
    ]
