# Generated by Django 2.0.2 on 2018-02-27 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id_description', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'description',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id_patient', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id_platform', models.AutoField(primary_key=True, serialize=False)),
                ('platform', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'platform',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id_stage', models.AutoField(primary_key=True, serialize=False)),
                ('stage', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'stage',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id_variant', models.AutoField(primary_key=True, serialize=False)),
                ('cdna', models.CharField(max_length=30)),
                ('protein', models.CharField(max_length=30)),
                ('genomic', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'variant',
            },
        ),
    ]
