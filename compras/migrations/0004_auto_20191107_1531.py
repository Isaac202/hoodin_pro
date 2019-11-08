# Generated by Django 2.2.5 on 2019-11-07 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compras', '0003_auto_20191103_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='codusuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='compras',
            name='codcliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.Clientes'),
        ),
    ]