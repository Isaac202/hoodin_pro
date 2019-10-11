# Generated by Django 2.2.5 on 2019-10-06 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0003_auto_20191006_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='biografia',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='documento_identidade',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='documento_tipo',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='estadocivil',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='homepage',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='nacionalidade',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='nif',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='passaporte',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='twitter',
        ),
        migrations.AddField(
            model_name='clientes',
            name='data_cadastro',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='senha',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Endreco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=8, null=True)),
                ('pais', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('codusuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_identidade', models.CharField(blank=True, max_length=50, null=True)),
                ('documento_tipo', models.CharField(blank=True, max_length=20, null=True)),
                ('passaporte', models.CharField(blank=True, max_length=50, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=20, null=True)),
                ('estadocivil', models.CharField(blank=True, max_length=1, null=True)),
                ('biografia', models.CharField(blank=True, max_length=5000, null=True)),
                ('nif', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('homepage', models.CharField(blank=True, max_length=100, null=True)),
                ('codusuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]