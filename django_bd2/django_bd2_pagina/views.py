import traceback
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # ignorar os tokens, etc
from django.template import loader
from .forms import JogadorForm, AcaoDisciplinarForm, ClubeForm, EquipaForm, CampeonatoForm,CampeonatoJogosEquipasForm
from .forms import EpocaForm, JogosForm, ModalidadesForm, PontuacoesForms, SubstituicoesForm,Tipos_acao_disciplinarForm
from .forms import Tipos_de_pontuacaoForm
from .models import Jogadores, Equipas, Campeonatos

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
            print (request.POST)
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


def create_clube(request):
        if request.method == "GET":
            form = ClubeForm()
            return render(request, 'create_clube.html', {'form': form})
        else:
            form = ClubeForm(request.POST)
            print (request.POST)
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

def create_acao_disciplinar(request):
        if request.method == "GET":
            form = AcaoDisciplinarForm()
            return render(request, 'create_acoesdisciplinares.html', {'form': form})
        else:
            form = AcaoDisciplinarForm(request.POST)
            print (request.POST)
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


def create_campeonato(request):
        if request.method == "GET":
            form = CampeonatoForm()
            return render(request, 'campeonato.html', {'form': form})
        else:
            form = CampeonatoForm(request.POST)
            print (request.POST)
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

def create_campeonatos_jogos_jquipas(request):
        if request.method == "GET":
            form = CampeonatoJogosEquipasForm()
            return render(request, 'campeonatos_jogos_equipas.html', {'form': form})
        else:
            form = CampeonatoJogosEquipasForm(request.POST)
            print (request.POST)
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


def create_epoca(request):
        if request.method == "GET":
            form = EpocaForm()
            return render(request, 'epoca.html', {'form': form})
        else:
            form = EpocaForm(request.POST)
            print (request.POST)
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

def create_jogo(request):
        if request.method == "GET":
            form = JogosForm()
            return render(request, 'jogo.html', {'form': form})
        else:
            form = JogosForm(request.POST)
            print (request.POST)
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

def create_modalidade(request):
        if request.method == "GET":
            form = ModalidadesForm()
            return render(request, 'modalidade.html', {'form': form})
        else:
            form = ModalidadesForm(request.POST)
            print (request.POST)
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


def create_pontuacao(request):
        if request.method == "GET":
                form = PontuacoesForms()
                return render(request, 'pontuacao.html', {'form': form})
        else:
            form = PontuacoesForms(request.POST)
            print (request.POST)
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


def create_subctituicao(request):
        if request.method == "GET":
                form = SubstituicoesForm()
                return render(request, 'substituicao.html', {'form': form})
        else:
            form = SubstituicoesForm(request.POST)
            print (request.POST)
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


def create_tipos_acao_disciplinar(request):
        if request.method == "GET":
                form = Tipos_acao_disciplinarForm()
                return render(request, 'tipo_acao_disciplinar.html', {'form': form})
        else:
            form = Tipos_acao_disciplinarForm(request.POST)
            print (request.POST)
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


def create_tipos_de_pontuacao(request):
        if request.method == "GET":
                form = Tipos_de_pontuacaoForm()
                return render(request, 'tipo_pontuacao.html', {'form': form})
        else:
            form = Tipos_de_pontuacaoForm(request.POST)
            print (request.POST)
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

#  Listas da NASA



def jogador_list(request):
    from django.db import connection
    c = connection.cursor()
    c.execute('select * from view2')
    row = c.fetchall()

    context = {'view2_list': row,'jogador_list': Jogadores.objects.all(),'equipas_list': Equipas.objects.all(),'campeonatos_list': Campeonatos.objects.all()}
    print (row[0][1])
    return render(request,"list.html",context)


