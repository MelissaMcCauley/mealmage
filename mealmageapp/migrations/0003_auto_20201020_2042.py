# Generated by Django 3.1.2 on 2020-10-21 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealmageapp', '0002_auto_20201020_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeddish',
            name='dish_type',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='storeddish',
            name='ingredient',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='storeddish',
            name='recipe',
            field=models.TextField(blank=True),
        ),
    ]
