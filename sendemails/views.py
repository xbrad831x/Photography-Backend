from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def email(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['data']
    name= content['name']
    email = content['email']
    hear = content['howdidyouhear']
    comment = content['comment']
    subject = 'New message from ' + name
    message = "Name: %s \n \n Email: %s \n \n How did you hear about me: %s \n \n Comment:\n %s" % (name, email, hear, comment)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mercadobrandon33@yahoo.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse('Sent!')
