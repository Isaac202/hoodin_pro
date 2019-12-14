# Generated by Django 2.2.5 on 2019-12-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigos_promocionais', '0002_auto_20191208_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratePromocionalCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveSmallIntegerField(default=1)),
                ('data_inicio', models.DateField(verbose_name='Data de inicio')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=11)),
                ('data_fim', models.DateField(verbose_name='Data de termino')),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('cnpjcpf', models.CharField(blank=True, max_length=18, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(blank=True, max_length=1, null=True)),
                ('generated', models.BooleanField(default=False, verbose_name='gerado')),
            ],
            options={
                'verbose_name': 'Gerar código promocional',
                'verbose_name_plural': 'Gerar códigos promocionais',
            },
        ),
        migrations.AddField(
            model_name='codigos_promocionais',
            name='resgate',
            field=models.BooleanField(default=False),
        ),
    ]