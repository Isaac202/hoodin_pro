# Generated by Django 2.2.5 on 2019-10-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20191006_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]