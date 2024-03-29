# Generated by Django 3.2.7 on 2021-10-07 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0039_dato_contrato_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato_contrato',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Contratos.dato_the_fives'),
        ),
        migrations.AlterField(
            model_name='dato_contrato',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Contratos.dato_proveedor'),
        ),
    ]
