# Generated by Django 2.2.5 on 2019-10-02 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registros',
            options={'ordering': ('-data',)},
        ),
        migrations.AlterField(
            model_name='registros',
            name='codcliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registros',
            name='codservico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicos.Servicos'),
        ),
        migrations.AlterField(
            model_name='registros',
            name='resumo_obra',
            field=models.TextField(max_length=5000),
        ),
    ]
