# Generated by Django 4.2.7 on 2023-11-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_manytables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
