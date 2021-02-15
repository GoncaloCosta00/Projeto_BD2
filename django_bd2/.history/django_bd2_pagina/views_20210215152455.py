import traceback
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # ignorar os tokens, etc
from django.template import loader
from .forms import JogadorForm, AcaoDisciplinarForm, ClubeForm, EquipaForm, CampeonatoForm,CampeonatoJogosEquipasForm
from .forms import EpocaForm, JogosForm, ModalidadesForm, PontuacoesForms, SubstituicoesForm,Tipos_acao_disciplinarForm
from .forms import Tipos_de_pontuacaoForm,JogamForm,Jogador_jogos_equipaForm,Jogos_jogadores_acoesdiscipForm,Pontuacoes_jogadores_jogosForm
from .models import Jogadores, Equipas, Campeonatos, Clube,AcoesDisciplinares,Campeonatos,CampeonatosJogosEquipas,Jogam,Modalidades,Pontuacoes,PontuacoesJogadoresJogos,Substituicoes,TipoAcaoDisciplinar,TipoPontuacao,Epocas
from .forms import *

# json encoder
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps as json_dumps


#  Listas da NASA



def jogador_list(request):
    from django.db import connection
    c = connection.cursor()
    c.execute('select * from view2')
    row = c.fetchall()
    
    c.execute('select (select nome from jogadores where jogadores.id_jogador = jogam.id_jogador) as "nome_jogador", id_equipa, id_jogador from jogam')
    row2 = c.fetchall()

    context = {'view2_list': row,
                                'jogador_list': Jogadores.objects.filter(status = 'True'),
                                'equipas_list': Equipas.objects.filter(status = 'True'),
                                'campeonatos_list': Campeonatos.objects.filter(status = 'True'),
                                'clubes_list': Clube.objects.filter(status = 'True'),
                                'acoesDisciplinares_list' : AcoesDisciplinares.objects.filter(status = 'True'),
                                'campeonatosJogosEquipas_list' : CampeonatosJogosEquipas.objects.filter(status = 'True'),
                                'jogam_list' : row2,
                                'modalidades_list' : Modalidades.objects.filter(status = 'True'),
                                'pontuacoes_list' : Pontuacoes.objects.filter(status = 'True'),
                                'pontuacoesJogadoresJogos_list' : PontuacoesJogadoresJogos.objects.filter(status = 'True'),
                                'substituicoes_list' : Substituicoes.objects.filter(status = 'True'),
                                'tipoAcaoDisciplinar_list' : TipoAcaoDisciplinar.objects.filter(status = 'True'),
                                'tipoPontuacao_list' : TipoPontuacao.objects.filter(status = 'True'),
                                'epocas_list' : Epocas.objects.filter(status = 'True')}
    print (row[0][1])
    return render(request,"list.html",context)



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
            
        return HttpResponse('esta a funcionar!')


def create_jogam(request):
        if request.method == "GET":
                form = JogamForm()
                return render(request, 'jogam.html', {'form': form})
        else:
            form = JogamForm(request.POST)
            print (request.POST)

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
            
        return HttpResponse('esta a funcionar!')        
        

def create_jogador_jogos_equipa(request):
        if request.method == "GET":
                form = Jogador_jogos_equipaForm()
                return render(request, 'jogador_jogos_equipa.html', {'form': form})
        else:
            form = Jogador_jogos_equipaForm(request.POST)
            print (request.POST)

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
            
        return HttpResponse('esta a funcionar!')        
        

def create_jogos_jogadores_acoesdiscip(request):
        if request.method == "GET":
                form = Jogos_jogadores_acoesdiscipForm()
                return render(request, 'jogos_jogadores_acoesdiscip.html', {'form': form})
        else:
            form = Jogos_jogadores_acoesdiscipForm(request.POST)
            print (request.POST)

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
            
        return HttpResponse('esta a funcionar!')  


def create_pontuacoes_jogadores_jogos(request):
        if request.method == "GET":
                form = Pontuacoes_jogadores_jogosForm()
                return render(request, 'pontuacoes_jogadores_jogos.html', {'form': form})
        else:
            form = Pontuacoes_jogadores_jogosForm(request.POST)
            print (request.POST)

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
            
        return HttpResponse('esta a funcionar!')  
        

def list(request):
    template = loader.get_template('update.html')

    return HttpResponse(template.render({}, request))


def update(request):
    if request.method == "GET":
        from django.db import connection
        c = connection.cursor()

        #obter tabela a editar
        tabela = request.GET.get("tabela", "")
        if tabela == "" :
            return HttpResponse("É necessário especificar uma tabela!")

        #obter colunas da tabela
        c.execute('select column_name from information_schema.columns where table_name = \'' + tabela + '\'')
        row = c.fetchall()

        #creating query
        
        query = "select "
        first = True
        for v in row :
            if v is not None:
                if first:
                    first = False
                else:
                    query = query + ", "
                query = query + str(v[0])

        query = query + " from " + tabela
        first = True
        for v in request.GET :
            #dados[str(v[0])] = 1
            if v != "tabela":
                if first:
                    query = query + " where "
                    first = False
                else:
                    query = query + " and "
                query = query + v + " = '" + request.GET.get(v, "") + "'"

        #obter dados a editar
        print(query)
        c.execute(query)
        data = c.fetchall()
        dados = {}

        if len(data) == 0:
            return HttpResponse("Não existem esses dados na tabela!")
        elif len(data) != 1:
            return HttpResponse("Existem demasiados dados com esses valores!")

        print(data)
        index = 0
        for v in row :
            if v is not None:
                if data[0][index] != None:
                    dados[str(v[0])] = data[0][index]
            index = index + 1

        print(tabela)
        print(dados)
        #selecao do formulario a usar
        form = None
        template = ""
        if tabela == "jogam":
            template = 'jogam.html'
            form = JogamForm(dados)
        elif tabela == "pontuacoes_jogadores_jogos":
            template = 'pontuacoes_jogadores_jogos.html'
            form = Pontuacoes_jogadores_jogosForm(dados)
        elif tabela == "jogos_jogadores_acoesdiscip":
            template = 'jogos_jogadores_acoesdiscip.html'
            form = Jogos_jogadores_acoesdiscipForm(dados)
        elif tabela == "jogador_jogos_equipa":
            template = 'jogador_jogos_equipa.html'
            form = Jogador_jogos_equipaForm(dados)
        elif tabela == "tipo_pontuacao":
            template = 'tipo_pontuacao.html'
            form = Tipos_de_pontuacaoForm(dados)
        elif tabela == "tipo_acao_disciplinar":
            template = 'tipo_acao_disciplinar.html'
            form = Tipos_acao_disciplinarForm(dados)
        elif tabela == "substituicoes":
            template = 'substituicao.html'
            form = SubstituicoesForm(dados)
        elif tabela == "pontuacoes":
            template = 'pontuacao.html'
            form = PontuacoesForms(dados)
        elif tabela == "modalidades":
            template = 'modalidade.html'
            form = ModalidadesForm(dados)
        elif tabela == "jogo":
            template = 'jogo.html'
            form = JogosForm(dados)
        elif tabela == "epocas":
            template = 'epoca.html'
            form = EpocaForm(dados)
        elif tabela == "campeonatos_jogos_equipas":
            template = 'campeonatos_jogos_equipas.html'
            form = CampeonatoJogosEquipasForm(dados)
        elif tabela == "campeonatos":
            template = 'campeonato.html'
            form = CampeonatoForm(dados)
        elif tabela == "acoes_disciplinares":
            template = 'create_acoesdisciplinares.html'
            form = AcaoDisciplinarForm(dados)
        elif tabela == "clube":
            template = 'create_clube.html'
            form = ClubeForm(dados)
        elif tabela == "equipas":
            template = 'create_equipas.html'
            form = EquipaForm(dados)
        elif tabela == "jogadores":
            template = 'jogador.html'
            form = JogadorForm(dados)
        else:
            return HttpResponse("Não é possível editar a tabela solicitada no momento!")

        return render(request, template, {'form': form})
    else:
        from django.db import connection
        c = connection.cursor()

        #obter tabela a editar
        tabela = request.GET.get("tabela", "")
        if tabela == "" :
            return HttpResponse("É necessário especificar uma tabela!")

        form = None
        template = ""
        dados = request.POST
        if tabela == "":
            return HttpResponse("Não é possível editar a tabela solicitada no momento!")

        #obter colunas da tabela
        c.execute('select column_name from information_schema.columns where table_name = \'' + tabela + '\'')
        row = c.fetchall()

        #creating query
        query = "update " + tabela + " set "
        first = True
        for v in dados :
            print(v)
            if v != "csrfmiddlewaretoken":
                if first:
                    first = False
                else:
                    query = query + ", "
                query = query + v + " = '" + dados.get(v, "") + "'"

        #adding the where 
        first = True
        for v in request.GET :
            #dados[str(v[0])] = 1
            if v != "tabela":
                if first:
                    query = query + " where "
                    first = False
                else:
                    query = query + " and "
                query = query + v + " = '" + request.GET.get(v, "") + "'"

        #obter dados a editar
        print(query)
        c.execute(query)

        return redirect("/list")
        #return HttpResponse('POST DONE')

    return HttpResponse('Pedido não permitido!!')

