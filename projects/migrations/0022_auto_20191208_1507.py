# Generated by Django 2.2.8 on 2019-12-08 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20191205_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneynecessity',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='timenecessity',
            name='comment',
        ),
    ]
