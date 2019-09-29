# Generated by Django 2.2.5 on 2019-09-29 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('precos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precos',
            name='codservico',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='servico', to='servicos.Servicos', verbose_name='Servico'),
        ),
        migrations.AlterField(
            model_name='precos',
            name='tipo_servico',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='precos',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]
