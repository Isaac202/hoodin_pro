# Generated by Django 2.2.5 on 2019-12-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0020_auto_20191214_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='registros',
            name='manter_arquivo',
            field=models.BooleanField(default=True),
        ),
    ]