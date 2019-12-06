# Generated by Django 2.2.5 on 2019-12-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0005_auto_20191206_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='extensoes',
            field=models.ManyToManyField(to='extensoes.Extensoes', verbose_name='Extensoes serviçoes'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='servico_digitalizacao',
            field=models.BooleanField(default=False),
        ),
    ]
