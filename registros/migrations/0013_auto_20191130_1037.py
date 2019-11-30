# Generated by Django 2.2.5 on 2019-11-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0012_auto_20191127_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registros',
            name='resumo_obra',
        ),
        migrations.AddField(
            model_name='arquivoregistro',
            name='resume',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='registros',
            name='codindicacao',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registros',
            name='codqrcode',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registros',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]