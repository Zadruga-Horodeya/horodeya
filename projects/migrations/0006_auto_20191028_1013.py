# Generated by Django 2.2.6 on 2019-10-28 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20191028_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='legal_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.LegalEntity'),
        ),
    ]
