# Generated by Django 2.2.8 on 2019-12-08 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rules.contrib.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20191208_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timesupport',
            old_name='note',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='timesupport',
            name='project',
        ),
        migrations.AddField(
            model_name='moneysupport',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesupport',
            name='necessity',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='supports', to='projects.TimeNecessity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timesupport',
            name='price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ThingSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('comment', models.TextField()),
                ('accepted', models.BooleanField(blank=True, null=True)),
                ('accepted_at', models.DateTimeField(blank=True, null=True)),
                ('delivered', models.BooleanField(blank=True, null=True)),
                ('delivered_at', models.DateTimeField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('necessity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supports', to='projects.ThingNecessity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(rules.contrib.models.RulesModelMixin, models.Model),
        ),
    ]
