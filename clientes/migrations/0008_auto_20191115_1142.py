# Generated by Django 2.2.5 on 2019-11-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20191115_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cnpjcpf',
            field=models.CharField(max_length=18, verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='documento_identidade',
            field=models.CharField(max_length=50, verbose_name='Documento de identificação'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='documento_tipo',
            field=models.CharField(max_length=20, verbose_name='Tipo de Documento'),
        ),
    ]
