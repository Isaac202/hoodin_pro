# Generated by Django 2.2.5 on 2019-12-08 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicacoes', '0003_merge_20191126_1736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicacoes',
            options={'ordering': ['nome'], 'verbose_name': 'Indicação', 'verbose_name_plural': 'Indicações'},
        ),
    ]
