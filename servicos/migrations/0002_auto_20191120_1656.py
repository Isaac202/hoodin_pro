# Generated by Django 2.2.5 on 2019-11-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extensoes', '0003_auto_20191120_1656'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServicosExtensoes',
        ),
        migrations.AddField(
            model_name='servicos',
            name='extensoes',
            field=models.ManyToManyField(to='extensoes.Extensoes', verbose_name='Extensoes serviçoes'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='codservico',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
