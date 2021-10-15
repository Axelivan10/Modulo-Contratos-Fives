from django.contrib import admin
from django.contrib.admin import ListFilter,DateFieldListFilter
from django.db.models.aggregates import Count
from Contratos.models import *
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin


class Dato_contratoAdmin(admin.ModelAdmin):
    list_display=("id","nombre_contrato",'Departamento',"empresa", "proveedor","fecha_inicio", "fecha_fin")
    fields=(("nombre_contrato","periodos"),("duracion_periodo","precio_periodo"),"fecha_inicio","fecha_fin","estado", "nombre_departamento","archivo","empresa","proveedor")
    filter_horizontal=("estado", "nombre_departamento", )
    search_fields=("id","nombre_contrato",)
    list_display_links=("nombre_contrato",)
    list_filter=("fecha_inicio", "fecha_fin")
    
    def Departamento(self, obj):
        return "\n".join([p.nombre for p in obj.nombre_departamento.all()])

class Dato_the_fivesAdmin(admin.ModelAdmin):
    list_display=("id","nombre_hotel","razon_social","razon_comercial","rfc", "nombre_representante")
    list_filter=("nombre_hotel", "razon_social","razon_comercial")
    search_fields=("id","razon_social","razon_comercial","rfc")
    list_display_links=("nombre_hotel",)

class Dato_proveedorAdmin(admin.ModelAdmin):
    list_display=("id","nombre_proveedor","nombre_fiscal","rfc", "email","telefono_empresa","nombre_representante")
    search_fields=("id","nombre_proveedor","nombre_fiscal","rfc", "email")
    list_display_links=("nombre_proveedor",)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","correo_encargado")
    list_display_links=("nombre",)


admin.site.register(Dato_proveedor,Dato_proveedorAdmin)
admin.site.register(Dato_contrato, Dato_contratoAdmin)
admin.site.register(Dato_the_fives,Dato_the_fivesAdmin)
admin.site.register(Estado)
admin.site.register(Departamento,DepartamentoAdmin)
 