# Generated by Django 2.2.5 on 2019-12-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicacoes', '0004_auto_20191208_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicacaoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_pai', models.CharField(max_length=200)),
                ('code_filho', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Indicação Cliente',
                'verbose_name_plural': 'Indicações Clientes',
            },
        ),
    ]