# Generated by Django 2.2.5 on 2019-12-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0014_auto_20191120_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='documento_tipo',
            field=models.CharField(choices=[('RG', 'RG'), ('CNH', 'CNH'), ('Seguro Social', 'Seguro Social'), ('Titulo de Eleitor', 'Titulo de Eleitor'), ('Conselho de Classe', 'Conselho de Classe'), ('Outros', 'Outros')], max_length=20, verbose_name='Tipo de Documento *'),
        ),
    ]