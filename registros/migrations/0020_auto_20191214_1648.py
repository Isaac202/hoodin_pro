# Generated by Django 2.2.5 on 2019-12-14 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0019_auto_20191208_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arquivoregistro',
            options={'verbose_name': 'Arquivo', 'verbose_name_plural': 'Arquivos'},
        ),
        migrations.AlterModelOptions(
            name='registros',
            options={'ordering': ('-data',), 'verbose_name': 'Registro', 'verbose_name_plural': 'Registros'},
        ),
    ]
