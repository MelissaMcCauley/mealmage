# Generated by Django 3.1.2 on 2020-10-23 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealmageapp', '0004_auto_20201021_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeddish',
            name='meal_type',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
