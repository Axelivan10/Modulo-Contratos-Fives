# Generated by Django 3.0.6 on 2021-10-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0035_auto_20211006_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato_contrato',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='imagenes/%Y/%m/%d'),
        ),
    ]
