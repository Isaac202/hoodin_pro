# Generated by Django 2.2.5 on 2019-09-13 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codservico', models.PositiveIntegerField()),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=11)),
                ('tamanho', models.PositiveIntegerField()),
                ('medida', models.CharField(max_length=5)),
                ('servico_digitalizacao', models.CharField(max_length=1)),
            ],
        ),
    ]
