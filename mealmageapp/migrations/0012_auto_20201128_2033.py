# Generated by Django 3.1.2 on 2020-11-29 01:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mealmageapp', '0011_auto_20201123_2040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailyMealPlan',
            new_name='DailyMenu',
        ),
    ]