# Generated by Django 2.2.8 on 2020-01-16 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_thingsupport_from_money_supports'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timesupport',
            unique_together={('necessity', 'user')},
        ),
    ]
