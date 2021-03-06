# Generated by Django 2.2.5 on 2019-12-04 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0015_auto_20191203_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='codigo_promocional',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Codigo Promocional'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='atuacao',
            field=models.ManyToManyField(blank=True, to='servicos.Servicos', verbose_name='AREA DE INTERESSE'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1, verbose_name='Sexo *'),
        ),
    ]
