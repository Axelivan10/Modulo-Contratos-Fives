from django.http import HttpResponse
from background_task import background
from django.contrib.auth.models import User
from django.shortcuts import render
from Contratos.models import *
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail
 
'''

@background(schedule=60)
def notify_user(user_id):
    # lookup user by id and send them a message
    user = User.objects.get(pk=user_id)
    user.email_user('Here is a notification', 'You have been notified')'''

'''
from django.core.mail import send_mail

defsend_mail(
    'Subject here',
    'Here is the message.',
    'axelivan02@gmail.com',
    ['1902088@utrivieramaya.edu.mx'],
    fail_silently=False,
)

'''

def vista(request):
    notify_user()
    return HttpResponse("HOLA MUNDO")


@background(schedule=20)
def notify_user():
    send_email_contrato()
    print("ya se envio esa mother")
    

def send_email_contrato():
    imprimir_vencidos=""
    correo = ""


    hoy = datetime.today()
    fecha_vencimiento= hoy + timedelta(days=30)
    dicc_vencidos = Dato_contrato.objects.filter(fecha_fin__range=[hoy,fecha_vencimiento])

    for impresion in dicc_vencidos:
            print(impresion)


    if dicc_vencidos.exists():
        #imprimir_vencidos= str(dicc_vencidos)
        for contrato in dicc_vencidos:
            if (contrato.nombre_departamento.count() > 0):

                for departamento in contrato.nombre_departamento.all(): 
                    print(departamento.nombre)
                    for correo in contrato.nombre_departamento.all():
                       #depa_nombre = correo.correo_encargado
                        print(correo.correo_encargado)
            
                    send_mail(
                    'RECORDATORIO CONTRATOS THE FIVES BEACH',
                    'Buen día, le recuerdo que el contrato ' + contrato.nombre_contrato  + ' del departamento de ' +
                    departamento.nombre + ' esta a punto de expirar',
                    settings.EMAIL_HOST_USER,
                    [correo.correo_encargado],
                    fail_silently=False
                    )
                    
                    
    else:
        print("NO TIENES CONTRATOS POR VENCER ")
        


'''
def send_email_contrato(user_id):
    nombre_contratos = Dato_contrato.objects.all()
    fiscal = Dato_contrato.objects.filter(id=9)
    email= Departamento.objects.filter(id=user_id)
    email2=  Departamento.objects.all()
    correo=""
    for nuevoemail  in email:
        correo= nuevoemail.correo_encargado

    print(nombre_contratos)
    print(email)
    print(fiscal)
    print(email2)
    for contratos in nombre_contratos:
        print(contratos.empresa.nombre_hotel)
    print(correo)
    str(correo)
    print(correo)
    send_mail(  
    'RECORDATORIO CONTRATOS',
    'Buen día, le recuerdo que el contrato esta a punto de expirar',
    settings.EMAIL_HOST_USER,
    [correo],
    fail_silently=False
    )




    for contratos in nombre_contratos:
        print(contratos.nombre_hotel)


  if Departamento.objects.filter(name=Departamento.nombre).count():

for dicc_vencidos in Dato_contrato.objects.filter(fecha_fin__range=[hoy,fecha_vencimiento]):
        print (dicc_vencidos)
        lista.append(dicc_vencidos)
    '''

