# Generated by Django 2.2.5 on 2019-09-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20190928_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='telefone',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='sexo',
            field=models.CharField(blank=True, choices=[('', ''), ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], default='', max_length=1, null=True),
        ),
    ]
