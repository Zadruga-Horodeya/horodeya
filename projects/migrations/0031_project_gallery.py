# Generated by Django 2.2.8 on 2020-01-13 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20190223_2138'),
        ('projects', '0030_project_primary_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='photologue.Gallery'),
        ),
    ]
