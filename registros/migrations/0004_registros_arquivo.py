# Generated by Django 2.2.5 on 2019-10-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_remove_registros_caminho_arquivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='registros',
            name='arquivo',
            field=models.FileField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
