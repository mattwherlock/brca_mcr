# Generated by Django 2.0.2 on 2018-03-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_auto_20180301_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='stage_str',
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
    ]
