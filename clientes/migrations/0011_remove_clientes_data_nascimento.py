# Generated by Django 2.2.5 on 2019-09-28 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_auto_20190928_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='data_nascimento',
        ),
    ]
