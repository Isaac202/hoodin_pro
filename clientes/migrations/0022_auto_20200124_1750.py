# Generated by Django 2.2.5 on 2020-01-24 17:50

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0021_auto_20200124_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='pais',
            field=django_countries.fields.CountryField(default='Brazil', max_length=2),
        ),
    ]
