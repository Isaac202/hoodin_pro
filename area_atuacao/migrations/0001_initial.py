# Generated by Django 2.2.5 on 2019-11-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area_Atuacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codarea', models.PositiveIntegerField(null=True)),
                ('nome', models.CharField(max_length=20)),
                ('texto', models.CharField(max_length=2500)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
