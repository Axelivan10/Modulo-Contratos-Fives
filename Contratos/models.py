from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import AutoField, CharField, IntegerField, TextField
from django.utils import tree
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE


'''class Proveedores(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, verbose_name= "Nombre Prooverdor")

    def __str__(self):
        return "{}".format(self.nombre )
    
    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'
        '''

'''
class Nombre_representante(models.Model):
    id=AutoField(primary_key=True)
    nombre_encargado=models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.nombre_encargado)

    class Meta:
        verbose_name='Representante'
        verbose_name_plural='Representantes'  
'''

class Estado(models.Model):
    id=AutoField(primary_key=True)
    estado=models.CharField(max_length=10,verbose_name= "Estado Contrato")

    def __str__(self):
        return "{}".format(self.estado)


class Departamento(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, verbose_name="Nombre Departamento")
    correo_encargado=models.EmailField(verbose_name="Correo Encargado")

    def __str__(self):
        return self.nombre

class Dato_proveedor(models.Model):
    id=models.AutoField(primary_key=True)
    nombre_proveedores=models.CharField(max_length=50,blank=True, null=True)
    nombre_fiscal=models.CharField(max_length=50)
    rfc=models.CharField(max_length=13)
    telefono_empresa=models.CharField(max_length=20)
    email=models.EmailField()
    nombre_representante=models.CharField(max_length=50, null=True, blank=True)
    telefono_representante=models.CharField(max_length=20)
    observaciones=models.TextField(max_length=200)

    def __str__(self):
        return self.nombre_proveedores+" / "+self.nombre_fiscal
   
    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'    


class Dato_the_fives(models.Model):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    id=models.AutoField(primary_key=True)
    nombre_hotel=models.CharField(max_length=50)
    razon_social=models.CharField(max_length=50, null=True)
    rfc=models.CharField(max_length=13, null=True)
    razon_comercial=models.CharField(max_length=50, null=True)
    nombre_representante=models.CharField(max_length=30)
    telefono_responsable=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_hotel+" / "+self.razon_social


    class Meta:
        verbose_name='Empresa The Five'  

class Dato_contrato(models.Model):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    id=models.AutoField(primary_key=True)
    nombre_contrato=models.CharField(max_length=30, )
    periodos=models.CharField(max_length=10, blank=True, null=True)
    duracion_periodo=models.CharField(max_length=20, blank=True, null=True)
    precio_periodo=models.CharField(max_length=20,blank=True, null=True)
    precio_final=models.CharField(max_length=30,blank=True, null=True)
    fecha_inicio=models.DateField(verbose_name="Fecha Inicio")
    fecha_fin=models.DateField(verbose_name="Fecha Fin")
    estado=models.ManyToManyField(Estado)
    nombre_departamento=models.ManyToManyField(Departamento)
    archivo = models.FileField('Contrato',upload_to='Contratos/%Y/%m', blank=True, null=True)
    fecha_subida_documento = models.DateTimeField(auto_now = True, blank=True, null=True)
    empresa=models.ForeignKey(Dato_the_fives, null=True, blank=True, on_delete=models.DO_NOTHING)
    proveedor=models.ForeignKey(Dato_proveedor, null=True, blank=True, on_delete=models.DO_NOTHING)


    def __str__(self):  
        return '{} {} {} {}'.format(self.id,self.nombre_contrato, self.fecha_inicio, self.fecha_fin)

    class Meta:
        verbose_name='Contrato'
        verbose_name_plural='Contratos'
 
