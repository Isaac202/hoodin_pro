# Generated by Django 2.2.5 on 2019-09-26 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20190924_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='codcliente',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='senha',
        ),
    ]
