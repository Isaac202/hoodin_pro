# Generated by Django 2.2.5 on 2019-09-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20190913_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'ordering': ('nome',)},
        ),
        migrations.AddField(
            model_name='clientes',
            name='senha',
            field=models.CharField(default='123456', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]