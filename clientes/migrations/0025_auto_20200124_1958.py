# Generated by Django 2.2.5 on 2020-01-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0024_merge_20200124_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1, null=True, verbose_name='Sexo *'),
        ),
    ]