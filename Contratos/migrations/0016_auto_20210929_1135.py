# Generated by Django 3.0.6 on 2021-09-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contratos', '0015_auto_20210929_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nombre_representante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_encargado', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='dato_empresa',
            name='nombre_responsable',
        ),
        migrations.RemoveField(
            model_name='dato_empresa',
            name='nombre_proveedores',
        ),
        migrations.AddField(
            model_name='dato_empresa',
            name='nombre_proveedores',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Proveedores',
        ),
        migrations.DeleteModel(
            name='Telefono_empresa',
        ),
        migrations.AddField(
            model_name='dato_empresa',
            name='nombre_representante',
            field=models.ManyToManyField(to='Contratos.Nombre_representante'),
        ),
    ]