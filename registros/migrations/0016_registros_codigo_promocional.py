# Generated by Django 2.2.5 on 2019-12-04 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0015_auto_20191203_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='registros',
            name='codigo_promocional',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Codigo Promocional'),
        ),
    ]
