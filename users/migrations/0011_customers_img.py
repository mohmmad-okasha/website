# Generated by Django 4.1.5 on 2023-02-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='img',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
