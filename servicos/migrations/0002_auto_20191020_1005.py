# Generated by Django 2.2.5 on 2019-10-20 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicosextensoes',
            name='codextensao',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='extensoes', to='extensoes.Extensoes', verbose_name='Extensoes'),
        ),
        migrations.AlterField(
            model_name='servicosextensoes',
            name='codservico',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]