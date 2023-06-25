# Generated by Django 4.1.6 on 2023-06-25 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dark_mode', models.BooleanField()),
                ('lang', models.CharField(max_length=50)),
                ('primary_color', models.CharField(max_length=50)),
                ('back_color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=300)),
                ('timestamp', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('url', models.CharField(max_length=50)),
                ('timestamp', models.CharField(blank=True, max_length=50)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.subjects')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
