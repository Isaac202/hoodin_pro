# Generated by Django 2.2.5 on 2019-11-01 15:37
# Generated by Django 2.2.5 on 2019-11-01 21:11


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area_atuacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area_atuacao',
            name='codarea',
            field=models.PositiveIntegerField(null=True),
        ),
    ]