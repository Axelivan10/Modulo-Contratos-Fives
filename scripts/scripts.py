from django.http import HttpResponse
from background_task import background
from django.contrib.auth.models import User
from django.shortcuts import render
from Contratos.models import *
from datetime import datetime, timedelta, date
from django.conf import settings
from django.core.mail import send_mail

dicc_vencidos= None
imprimir_fecha=""

def vista(request):
    notify_user()
    return HttpResponse("HOLA MUNDO")


#@background(schedule=20)
def notify_user():
    send_email_contrato()
    print("ya se envio esa mother")
    

def send_email_contrato():
    hoy = date.today()
    fecha_vencimiento30= hoy + timedelta(days=30)
    fecha_vencimiento25= hoy + timedelta(days=25)
    fecha_vencimiento20= hoy + timedelta(days=20)
    #dicc_vencidos = Dato_contrato.objects.filter(fecha_fin__range=[hoy,fecha_vencimiento])
    dicc_vencidos = Dato_contrato.objects.filter(fecha_fin__year=fecha_vencimiento30.year,
                                                 fecha_fin__month=fecha_vencimiento30.month,
                                                 fecha_fin__day=fecha_vencimiento30.day) | Dato_contrato.objects.filter(fecha_fin__year=fecha_vencimiento25.year,
                                                 fecha_fin__month=fecha_vencimiento25.month,
                                                 fecha_fin__day=fecha_vencimiento25.day) | Dato_contrato.objects.filter(fecha_fin__year=fecha_vencimiento20.year,
                                                 fecha_fin__month=fecha_vencimiento20.month,
                                                 fecha_fin__day=fecha_vencimiento20.day)

    print(dicc_vencidos)
    if dicc_vencidos.exists():
        #imprimir_vencidos= str(dicc_vencidos)
        for contrato in dicc_vencidos:
            if (contrato.nombre_departamento.count() > 0):
                for departamento in contrato.nombre_departamento.all(): 
                    print(departamento.nombre)
                    for correo in contrato.nombre_departamento.all():
                       #depa_nombre = correo.correo_encargado
                        print(correo.correo_encargado)

                    imprimir_fecha= str(contrato.fecha_fin)
                    send_mail(
                    'RECORDATORIO CONTRATOS THE FIVES BEACH',
                    f'A quien corresponda,\n \nSe le recuerda que el contrato de proveedores de The Fives con los siguientes datos: \n \nNombre: {contrato.nombre_contrato.upper()} \nDepartamento: {departamento.nombre.upper()} \nHotel: {contrato.empresa.nombre_hotel.upper()} \nProveedor: {contrato.proveedor.nombre_proveedor.upper()} \nFecha de vencimiento: {imprimir_fecha} \n \nSaludos condiales, \nThe Fives'
                    ,
                    settings.EMAIL_HOST_USER,
                    [correo.correo_encargado],
                    fail_silently=False
                    )
                    
                    
    else:
        print("NO TIENES CONTRATOS POR VENCER ")

'''
def contrato_check():
    if dicc_vencidos.exists():
        #imprimir_vencidos= str(dicc_vencidos)
        for contrato in dicc_vencidos:
            if (contrato.nombre_departamento.count() > 0):

                for departamento in contrato.nombre_departamento.all(): 
                    print(departamento.nombre)
                    for correo in contrato.nombre_departamento.all():
                       #depa_nombre = correo.correo_encargado
                        print(correo.correo_encargado)

                        
                    imprimir_fecha= str(contrato.fecha_fin)
                    send_mail(
                    'RECORDATORIO CONTRATOS THE FIVES BEACH',
                    'Buen día, le recuerdo que el contrato con nombre: ' + contrato.nombre_contrato.upper()+ ' del departamento: ' +
                    departamento.nombre.upper() + ' esta a punto de expirar en la fecha de:  '+ imprimir_fecha,
                    settings.EMAIL_HOST_USER,
                    [correo.correo_encargado],
                    fail_silently=False
                    )
                    
                    
    else:
        print("NO TIENES CONTRATOS POR VENCER ")
        



'''



 #'RECORDATORIO CONTRATOS THE FIVES BEACH',
  #                  f'''A quien corresponda, se le recuerda que el contrato de proveedores de The Fives con los siguientes datos:
   #                 Nombre:{contrato.nombre_contrato}
    #                Departamento: {departamento.nombre}
     #               Hotel:{contrato.empresa.nombre_hotel}
      #              Proveedor:{contrato.proveedor.nombre_proveedor}
       #             Fecha de vencimiento:{imprimir_fecha}
        #            Saludos condiales,
         #           The Fives
          #          ''',