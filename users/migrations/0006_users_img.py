# Generated by Django 4.1.5 on 2023-02-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_test_model_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='img',
            field=models.ImageField(blank=True, default='1.jpg', upload_to=''),
        ),
    ]