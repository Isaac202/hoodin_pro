# Generated by Django 2.2.5 on 2019-11-11 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_registros_codusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registros',
            name='codcliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Clientes'),
        ),
    ]