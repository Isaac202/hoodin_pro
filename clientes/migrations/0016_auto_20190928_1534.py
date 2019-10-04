# Generated by Django 2.2.5 on 2019-09-28 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicacoes', '0003_remove_indicacoes_codindicacao'),
        ('clientes', '0015_auto_20190928_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='biografia',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='codindicacao',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='indicacao', to='indicacoes.Indicacoes', verbose_name='Indicacao'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='estadocivil',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='homepage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='nif',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='passaporte',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clientes',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]