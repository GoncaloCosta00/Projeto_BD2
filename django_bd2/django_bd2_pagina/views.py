import traceback
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # ignorar os tokens, etc
from django.template import loader
from .forms import JogadorForm
<<<<<<< HEAD
from .models import Jogadores, Equipas

=======
from .forms import EquipaForm
from .models import Jogadores
>>>>>>> main


# json encoder
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps as json_dumps


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def create(request):
    template = loader.get_template('create.html')

    return render(request, 'create.html', {})

# def create_jogador(request):
#    template = loader.get_template('jogador.html')
#
#    return HttpResponse(template.render({},request))


def create_jogador(request):
    if request.method == "GET":
        form = JogadorForm()
        return render(request, 'jogador.html', {'form': form})
    else:
        form = JogadorForm(request.POST)
        # else:
        #    employee = Employee.objects.get(pk=id)
        #    form = JogadorForm(request.POST,instance= employee)
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
            except Exception as e:
                trace_back = traceback.format_exc()
                message = str(e)+ " " + str(trace_back)
                print (message)

            return HttpResponse('1')
        # return redirect('/create')
        return HttpResponse('esta a funcionar!')


def create_equipa(request):
        if request.method == "GET":
            form = EquipaForm()
            return render(request, 'create_equipas.html', {'form': form})
        else:
            form = EquipaForm(request.POST)
            # else:
            #    employee = Employee.objects.get(pk=id)
            #    form = JogadorForm(request.POST,instance= employee)
            if form.is_valid():
                try:
                    obj = form.save(commit=False)
                    obj.user = request.user
                    obj.save()
                except Exception as e:
                    trace_back = traceback.format_exc()
                    message = str(e)+ " " + str(trace_back)
                    print (message)

                return HttpResponse('1')
            # return redirect('/create')
        return HttpResponse('esta a funcionar!')


def list(request):
    template = loader.get_template('update.html')

    return HttpResponse(template.render({}, request))


def update(request):
    template = loader.get_template('list.html')

<<<<<<< HEAD
#  Listas da NASA
def jogador_list(request):
    context = {'jogador_list': Jogadores.objects.all(),'equipas_list': Equipas.objects.all()}
    return render(request,"list.html",context)





=======
    return HttpResponse(template.render({}, request))
>>>>>>> main
