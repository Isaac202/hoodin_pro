# Generated by Django 2.2.5 on 2021-01-20 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituicoes', '0001_initial'),
        ('avaliadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliadores',
            name='id_instituicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='instituicoes.Instituicoes'),
        ),
    ]