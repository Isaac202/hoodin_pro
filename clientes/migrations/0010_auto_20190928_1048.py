# Generated by Django 2.2.5 on 2019-09-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20190928_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='sexo',
        ),
        migrations.AddField(
            model_name='clientes',
            name='celular',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='telefone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]