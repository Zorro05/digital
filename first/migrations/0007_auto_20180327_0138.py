# Generated by Django 2.0.2 on 2018-03-26 22:38

from django.db import migrations, models
import django.db.models.deletion
import first.models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_auto_20180318_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=200, null=True)),
                ('lecture_title', models.CharField(blank=True, max_length=200, null=True)),
                ('language', models.CharField(blank=True, max_length=200, null=True)),
                ('this_lect_is', models.CharField(blank=True, max_length=200, null=True)),
                ('is_consired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('platform_country', models.CharField(blank=True, max_length=200, null=True)),
                ('platform_city', models.CharField(blank=True, max_length=200, null=True)),
                ('platform_adress', models.CharField(blank=True, max_length=200, null=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='lectures',
        ),
        migrations.AddField(
            model_name='org',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='org',
            name='director',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='org',
            name='director_email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='org',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=first.models.avatar_upload_to),
        ),
        migrations.AddField(
            model_name='org',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='org',
            name='resperative',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='academic_rank',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, default='United States', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='orc_id',
            field=models.URLField(blank=True, default='None', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='placeOfWork',
            field=models.CharField(blank=True, default='None', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='position',
            field=models.CharField(blank=True, default='Professor', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='researcher_id',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='science_degree',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='scientific_interest',
            field=models.CharField(blank=True, default='None', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='sex',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='org',
            name='lecture_themes',
        ),
        migrations.AddField(
            model_name='org',
            name='lecture_themes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.AddField(
            model_name='platform',
            name='Org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Account'),
        ),
        migrations.AddField(
            model_name='app',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Platform'),
        ),
        migrations.AddField(
            model_name='app',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Account'),
        ),
    ]
