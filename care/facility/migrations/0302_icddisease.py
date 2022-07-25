# Generated by Django 2.2.11 on 2022-07-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0301_auto_20220709_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='ICDDisease',
            fields=[
                ('id', models.CharField(max_length=1024, primary_key=True, serialize=False, unique=True)),
                ('label', models.CharField(max_length=1024)),
                ('is_leaf', models.BooleanField(default=False)),
                ('class_kind', models.CharField(max_length=1024)),
                ('is_adopted_child', models.BooleanField(default=False)),
                ('average_depth', models.FloatField()),
                ('parent_id', models.CharField(max_length=1024, null=True)),
            ],
        ),
    ]
