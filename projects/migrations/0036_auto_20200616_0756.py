# Generated by Django 2.2.8 on 2020-06-16 04:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_auto_20200610_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True, verbose_name='answer'),
        ),
        migrations.AlterField(
            model_name='community',
            name='DDORegistration',
            field=models.BooleanField(default=False, verbose_name='DDORegistration'),
        ),
        migrations.AlterField(
            model_name='community',
            name='activityType',
            field=models.CharField(choices=[('Creativity', ' Проекти от областта на науката или изкуството, които развиват градивната енергия на индивида и неговата сила за себе реализация.'), ('Education', 'Проекти, стъпили на принципа на висшата справедливост и въплащение на благородни мисли и желания в живота на човека, при което интуитивните и творческите му способности достигат нови нива.'), ('Art', ' Проекти в областта на културата, които събуждат естественото ни чувство за споделяне и придават финес на взаимоотношенията в обществото.'), ('Administration', 'Проекти, свързани със системи за създаване и прилагане на правила за истинно и честно социално взаимодействие. Механизми за разрешаване на спорове.'), ('Willpower', 'Проекти, които развиват смелост, устрем, воля за победа, воля за индивидуална и колективна изява, като спорт и туризъм.'), ('Health', 'Проекти, които следват естествения ритъм на човешкия организъм и са мост между Висшия и конкретния ум.'), ('Food', 'Проекти развиващи това, което най-пряко влияе върху нашите бит и ежедневие, допринасят за оцеляването и изхранването на обществото.')], default='Art', max_length=50, verbose_name='activityType'),
        ),
        migrations.AlterField(
            model_name='community',
            name='bulstat',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True, verbose_name='bulstat'),
        ),
        migrations.AlterField(
            model_name='community',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='community',
            name='facebook_page',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='facebook_page'),
        ),
        migrations.AlterField(
            model_name='community',
            name='mission',
            field=models.TextField(default=None, null=True, verbose_name='mission'),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='community',
            name='numberOfSupporters',
            field=models.IntegerField(default=0, verbose_name='numberOfSupporters'),
        ),
        migrations.AlterField(
            model_name='community',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=20, null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='community',
            name='previousExperience',
            field=models.TextField(blank=True, verbose_name='previousExperience'),
        ),
        migrations.AlterField(
            model_name='community',
            name='slack_channel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slack_channel'),
        ),
        migrations.AlterField(
            model_name='community',
            name='text',
            field=models.TextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='community',
            name='type',
            field=models.CharField(default='НПО', max_length=50, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='community',
            name='website',
            field=models.CharField(blank=True, max_length=100, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='TIN',
            field=models.CharField(max_length=10, verbose_name='TIN'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='birthdate',
            field=models.DateField(verbose_name='birthdate'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='citizenship',
            field=django_countries.fields.CountryField(max_length=30, verbose_name='citizenship'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='domicile',
            field=django_countries.fields.CountryField(max_length=30, verbose_name='domicile'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='passportData',
            field=models.CharField(max_length=30, verbose_name='passportData'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='placeOfBirth',
            field=models.CharField(max_length=30, verbose_name='placeOfBirth'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='postAddress',
            field=models.CharField(max_length=20, verbose_name='postAdress'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='profession',
            field=models.CharField(max_length=30, verbose_name='profession'),
        ),
        migrations.AlterField(
            model_name='donatordata',
            name='website',
            field=models.CharField(blank=True, max_length=30, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='legalentitydonatordata',
            name='DDORegistration',
            field=models.BooleanField(verbose_name='DDORegistration'),
        ),
        migrations.AlterField(
            model_name='legalentitydonatordata',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='legalentitydonatordata',
            name='phoneNumber',
            field=models.CharField(max_length=30, verbose_name='phoneNumber'),
        ),
        migrations.AlterField(
            model_name='legalentitydonatordata',
            name='type',
            field=models.CharField(max_length=50, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='legalentitydonatordata',
            name='website',
            field=models.CharField(blank=True, max_length=30, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='moneysupport',
            name='status',
            field=models.CharField(choices=[('review', 'review'), ('delivered', 'delivered'), ('accepted', 'accepted'), ('declined', 'declined'), ('expired', 'expired')], default='review', max_length=20, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='moneysupport',
            name='status_since',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='status_since'),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Creativity', 'Наука и творчество'), ('Education', 'Просвета и възпитание'), ('Art', 'Култура и артистичност'), ('Administration', 'Администрация и финанси'), ('Willpower', 'Спорт и туризъм'), ('Health', 'Бит и здравеопазване'), ('Food', 'Земеделие и изхранване')], default='Education', max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Community', verbose_name='Community'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=300, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name='end_date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date_tasks',
            field=models.DateField(null=True, verbose_name='end_date_tasks'),
        ),
        migrations.AlterField(
            model_name='project',
            name='goal',
            field=models.TextField(null=True, verbose_name='goal'),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(max_length=30, null=True, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='report_period',
            field=models.CharField(choices=[('weekly', 'weekly'), ('montly', 'montly'), ('twoweeks', 'twoweeks')], default='weekly', max_length=50, verbose_name='report_period'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slack_channel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slack_channel'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True, verbose_name='start_date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='project',
            name='verified_status',
            field=models.CharField(choices=[('review', 'review'), ('accepted', 'accepted'), ('rejected', 'rejected')], default=None, max_length=20, null=True, verbose_name='verified_status'),
        ),
        migrations.AlterField(
            model_name='question',
            name='required',
            field=models.BooleanField(default=True, verbose_name='required'),
        ),
        migrations.AlterField(
            model_name='questionprototype',
            name='required',
            field=models.BooleanField(default=True, verbose_name='required'),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='report',
            name='published_at',
            field=models.DateTimeField(verbose_name='published_at'),
        ),
        migrations.AlterField(
            model_name='report',
            name='text',
            field=models.TextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='thingnecessity',
            name='count',
            field=models.IntegerField(verbose_name='count'),
        ),
        migrations.AlterField(
            model_name='thingnecessity',
            name='description',
            field=models.CharField(max_length=300, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='thingnecessity',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='thingnecessity',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='thingsupport',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='thingsupport',
            name='status',
            field=models.CharField(choices=[('review', 'review'), ('delivered', 'delivered'), ('accepted', 'accepted'), ('declined', 'declined'), ('expired', 'expired')], default='review', max_length=20, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='thingsupport',
            name='status_since',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='status_since'),
        ),
        migrations.AlterField(
            model_name='timenecessity',
            name='count',
            field=models.IntegerField(default=1, verbose_name='count'),
        ),
        migrations.AlterField(
            model_name='timenecessity',
            name='description',
            field=models.CharField(max_length=300, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='timenecessity',
            name='end_date',
            field=models.DateField(verbose_name='end_date'),
        ),
        migrations.AlterField(
            model_name='timenecessity',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='timenecessity',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='timenecessity',
            name='start_date',
            field=models.DateField(verbose_name='start_date'),
        ),
        migrations.AlterField(
            model_name='timesupport',
            name='end_date',
            field=models.DateField(verbose_name='end_date'),
        ),
        migrations.AlterField(
            model_name='timesupport',
            name='price',
            field=models.IntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='timesupport',
            name='start_date',
            field=models.DateField(verbose_name='start_date'),
        ),
        migrations.AlterField(
            model_name='timesupport',
            name='status',
            field=models.CharField(choices=[('review', 'review'), ('delivered', 'delivered'), ('accepted', 'accepted'), ('declined', 'declined'), ('expired', 'expired')], default='review', max_length=20, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='timesupport',
            name='status_since',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='status_since'),
        ),
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='second_name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='slack_channel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slack_channel'),
        ),
    ]