# Generated by Django 2.2.5 on 2019-12-08 11:35

from django.db import migrations, models
import registros.models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0018_remove_registros_codindicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivoregistro',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=registros.models.user_directory_path),
        ),
    ]
