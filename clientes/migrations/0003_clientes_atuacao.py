# Generated by Django 2.2.5 on 2019-11-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
        ('clientes', '0002_clientes_codusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='atuacao',
            field=models.ManyToManyField(blank=True, null=True, to='servicos.Servicos'),
        ),
    ]