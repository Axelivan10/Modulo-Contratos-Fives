# Generated by Django 3.2.7 on 2021-10-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0047_auto_20211015_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='estado',
            field=models.CharField(max_length=20, verbose_name='Estado Contrato'),
        ),
    ]