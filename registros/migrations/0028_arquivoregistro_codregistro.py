# Generated by Django 2.2.5 on 2020-01-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0027_arquivoregistro_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivoregistro',
            name='codregistro',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]