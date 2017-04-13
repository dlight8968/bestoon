from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import Expence , Income , Token , User
from datetime import datetime


# Create your views here.


@csrf_exempt
def submit_expence (request) :
    '''user submits an expence '''
    #TODO: user might be faked , amount might be invalid, vallidate data,token might be faked
    this_token = request.POST['token']
    thsi_user = User.objects.filter(token__token= this_token).get()
    if 'date' not in request.POST :
        now =datetime.now()
    Expence.objects.create(user = thsi_user , amount = request.POST['amount'] ,
    text = request.POST['text'],date = now)
    return JsonResponse({
    'status' : 'ok'
    } , encoder=JSONEncoder)


@csrf_exempt
def submit_income (request) :
    '''user submits an income '''

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST :
        now = datetime.now()
    Income.objects.create(user = this_user , amount = request.POST['amount'],
                text = request.POST['text'], date=now)
    return JsonResponse({
    'status' : 'ok'
    } , encoder =JSONEncoder)
