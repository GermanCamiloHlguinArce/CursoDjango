from django.http import HttpResponse

from datetime import datetime
import json

def hello_world(request):
    now=datetime.now().strftime('%b, %dth, %Y - %H:%M hrs')
    return HttpResponse('oh, hi! Current server time is {now}'.format(now=str(now)))

def sorted(request):
    numbers=[int(position) for position in request.GET['numbers'].split(',')]
    orderNumber= sorted(numbers)
    data ={
        'status': 'ok',
        'numbers':orderNumber,
        'message': 'Integer sorted successfully.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if age <- 12:
        message ='Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, Welcome to Platzigram'.format(name)
    
    return HttpResponse(message)