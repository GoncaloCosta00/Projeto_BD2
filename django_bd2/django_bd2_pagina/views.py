from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt #ignorar os tokens, etc
from django.template import loader

#json encoder
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps as json_dumps


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def create(request):
    template = loader.get_template('create.html')
  
    return render(request,'create.html',{})

def list(request):
    template = loader.get_template('update.html')
  
    return HttpResponse(template.render({},request))

def update(request):
    template = loader.get_template('list.html')
  
    return HttpResponse(template.render({},request))


