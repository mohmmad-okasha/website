# Generated by Django 4.1.5 on 2023-02-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_customers_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='img',
            field=models.CharField(max_length=100),
        ),
    ]
