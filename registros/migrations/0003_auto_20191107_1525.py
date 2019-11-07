# Generated by Django 2.2.5 on 2019-11-07 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registros', '0002_auto_20191101_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='registros',
            name='codusuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registros',
            name='codcliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.Clientes'),
        ),
    ]
