from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt #ignorar os tokens, etc
from django.template import loader
from .forms import JogadorForm
from .models import Jogadores


#json encoder
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps as json_dumps


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def create(request):
    template = loader.get_template('create.html')
  
    return render(request,'create.html',{})

#def create_jogador(request):
#    template = loader.get_template('jogador.html')
#  
#    return HttpResponse(template.render({},request))

def create_jogador(request):
    #if request.method == "POST":
        form = JogadorForm()
        if form.is_valid():
            form.save()
        else:   
            form = JogadorForm()
        return render(request, 'jogador.html', {'form': form})
    #return HttpResponse("Não é isto que pretendes")

def list(request):
    template = loader.get_template('update.html')
  
    return HttpResponse(template.render({},request))

def update(request):
    template = loader.get_template('list.html')
  
    return HttpResponse(template.render({},request))



