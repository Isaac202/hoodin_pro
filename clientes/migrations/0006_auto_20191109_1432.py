# Generated by Django 2.2.5 on 2019-11-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_clientes_codindicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='tipo_pessoa',
            field=models.CharField(blank=True, choices=[('J', 'Juridica'), ('F', 'Fisica')], max_length=1, null=True),
        ),
    ]
