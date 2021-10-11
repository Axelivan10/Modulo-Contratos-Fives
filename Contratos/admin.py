from django.contrib import admin
from django.contrib.admin import ListFilter
from Contratos.models import *
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin
    
'''
class Dato_contratoAdmin(admin.ModelAdmin):
    list_display=("id","nombre_contrato","fecha_inicio", "fecha_fin")
    list_filter=("nombre_contrato", "fecha_inicio", "fecha_fin",)
    '''


class Dato_contratoAdmin(admin.ModelAdmin):
    list_display=("id","nombre_contrato","fecha_inicio", "fecha_fin", "fecha_subida_documento")
    fields=(("nombre_contrato","periodos"),("duracion_periodo","precio_periodo"),"fecha_inicio","fecha_fin","estado", "nombre_departamento","archivo","empresa","proveedor")
    filter_horizontal=("estado", "nombre_departamento", )

class Dato_the_fivesAdmin(admin.ModelAdmin):
    list_display=("id","nombre_hotel","razon_social", "nombre_representante")
    list_filter=("nombre_hotel", "razon_social",)

class Dato_proveedorAdmin(admin.ModelAdmin):
    list_display=("id","nombre_fiscal","rfc", "email","telefono_empresa")
    list_filter=("nombre_fiscal","rfc",)
    search_fields=("id","nombre_hotel")

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","correo_encargado")
    list_filter=("id","nombre",)


admin.site.register(Dato_proveedor,Dato_proveedorAdmin)
admin.site.register(Dato_contrato, Dato_contratoAdmin)
admin.site.register(Dato_the_fives,Dato_the_fivesAdmin)
admin.site.register(Estado)
admin.site.register(Departamento,DepartamentoAdmin)
 