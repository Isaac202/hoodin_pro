# Generated by Django 2.2.5 on 2019-11-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extensoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extensoes',
            name='nome',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
