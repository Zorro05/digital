# Generated by Django 2.0.2 on 2018-03-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('first', '0005_account_placeofwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='placeOfWork',
            field=models.CharField(max_length=300),
        ),
    ]
