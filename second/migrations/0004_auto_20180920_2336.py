# Generated by Django 2.1.1 on 2018-09-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0003_flags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flags',
            name='flag',
        ),
        migrations.AddField(
            model_name='flags',
            name='code',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
