# Generated by Django 2.2.5 on 2019-11-20 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_compras_codusuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compras',
            old_name='codcliente',
            new_name='id_cliente',
        ),
    ]
