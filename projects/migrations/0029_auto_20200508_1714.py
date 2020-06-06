# Generated by Django 2.2.8 on 2020-05-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20200506_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='goal1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='goal2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='goal3',
        ),
        migrations.AddField(
            model_name='project',
            name='goal',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Creativity', 'Наука и творчество'), ('Education', 'Просвета и възпитание'), ('Art', 'Култура и артистичност'), ('Administration', 'Администрация и финанси'), ('Willpower', 'Спорт и туризъм'), ('Health', 'Бит и здравеопазване'), ('Food', 'Земеделие и изхранване')], default='Education', max_length=50),
        ),
    ]