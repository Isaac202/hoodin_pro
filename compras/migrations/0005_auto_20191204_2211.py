# Generated by Django 2.2.5 on 2019-12-04 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20191120_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='forma_pagamento',
            field=models.CharField(choices=[('Cartão de Crédito', 'Cartão de Crédito'), ('Cartão de Débito', 'Cartão de Débito')], default='Cartão de Crédito', max_length=30),
        ),
    ]
