# Generated by Django 3.0.6 on 2021-09-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0005_auto_20210928_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dato_empresa',
            name='contrato',
        ),
        migrations.AlterField(
            model_name='dato_contrato',
            name='precio_acordado',
            field=models.IntegerField(verbose_name='Precio Servicio'),
        ),
        migrations.AlterField(
            model_name='dato_empresa',
            name='tel_empresa',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dato_empresa',
            name='tel_responsable',
            field=models.IntegerField(),
        ),
    ]
