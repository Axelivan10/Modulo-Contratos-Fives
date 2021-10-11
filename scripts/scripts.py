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

def wenas(request, name):
    notify_user(name)
    return HttpResponse("HOLA MUNDO"+ name)


@background(schedule=20)
def notify_user(user_id):
    send_email_contrato(user_id)
    print("ya se envio esa mother")
    

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

