# Generated by Django 3.0.6 on 2021-10-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0031_auto_20211004_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='dato_contrato',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='media/imagenes'),
        ),
    ]
