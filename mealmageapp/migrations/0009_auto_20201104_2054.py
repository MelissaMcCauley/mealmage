# Generated by Django 3.1.2 on 2020-11-05 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealmageapp', '0008_auto_20201102_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storeddish',
            old_name='ingredient',
            new_name='ingredient01',
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient02',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient03',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient04',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient05',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient06',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient07',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient08',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient09',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient10',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient11',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient12',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient13',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient14',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient15',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='storeddish',
            name='ingredient16',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
