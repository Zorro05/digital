# Generated by Django 2.1.1 on 2018-09-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0006_auto_20180922_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='contact_person',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
