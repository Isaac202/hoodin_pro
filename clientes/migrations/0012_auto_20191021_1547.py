# Generated by Django 2.2.5 on 2019-10-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_auto_20191021_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='estadocivil',
            field=models.CharField(blank=True, choices=[('C', 'Casado'), ('S', 'Solteiro'), ('D', 'Divorciado'), ('V', 'Viuvo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='homepage',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tipo_pessoa',
            field=models.CharField(blank=True, choices=[('', ''), ('J', 'Juridica'), ('F', 'Fisica')], max_length=1, null=True),
        ),
    ]
