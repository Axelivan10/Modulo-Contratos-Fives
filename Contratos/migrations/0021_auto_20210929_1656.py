# Generated by Django 3.0.6 on 2021-09-29 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0020_auto_20210929_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato_contrato',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Contratos.Dato_the_fives'),
        ),
        migrations.AlterField(
            model_name='dato_contrato',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Contratos.Dato_proveedor'),
        ),
    ]