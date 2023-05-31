# Generated by Django 4.1.5 on 2023-05-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_color_settings_back_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('debit', models.FloatField(max_length=10)),
                ('credit', models.FloatField(max_length=10)),
                ('user', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='customers',
            name='user',
            field=models.CharField(default='NULL', max_length=50),
            preserve_default=False,
        ),
    ]