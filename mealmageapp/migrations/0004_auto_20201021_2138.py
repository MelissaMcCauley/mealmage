# Generated by Django 3.1.2 on 2020-10-22 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mealmageapp', '0003_auto_20201020_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grocerylist',
            old_name='ingredient_name',
            new_name='grocery_list_item',
        ),
    ]
