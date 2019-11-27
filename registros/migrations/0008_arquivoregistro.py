# Generated by Django 2.2.5 on 2019-11-27 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registros.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registros', '0007_auto_20191120_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivoRegistro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shar256', models.CharField(max_length=90)),
                ('file', models.FileField(upload_to=registros.models.user_directory_path)),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('signature', models.FileField(blank=True, null=True, upload_to='')),
                ('version', models.DecimalField(decimal_places=2, default=1.0, max_digits=9)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]