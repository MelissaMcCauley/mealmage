# Generated by Django 3.1.2 on 2020-10-21 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealmageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storeddish',
            options={'verbose_name_plural': 'Stored Dishes'},
        ),
        migrations.AlterField(
            model_name='storeddish',
            name='dish_type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='storeddish',
            name='ingredient',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='storeddish',
            name='recipe',
            field=models.TextField(default=''),
        ),
    ]
