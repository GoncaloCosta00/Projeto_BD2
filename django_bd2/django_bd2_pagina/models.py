from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class AcoesDisciplinares(models.Model):
    id_acao_disciplinar = models.AutoField(primary_key=True)
    id_tipo_acao_disciplinar = models.ForeignKey('TipoAcaoDisciplinar', models.DO_NOTHING, db_column='id_tipo_acao_disciplinar')
    comentario = models.TextField(blank=True, null=True)
    tempo_jogo = models.CharField(max_length=256)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acoes_disciplinares'


class Campeonatos(models.Model):
    id_campeonato = models.AutoField(primary_key=True)
    id_modalidade = models.ForeignKey('Modalidades', models.DO_NOTHING, db_column='id_modalidade')
    id_epoca = models.ForeignKey('Epocas', models.DO_NOTHING, db_column='id_epoca')
    nome_campeonato = models.TextField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campeonatos'


class CampeonatosJogosEquipas(models.Model):
    id_jogo = models.ForeignKey('Jogos', models.DO_NOTHING, db_column='id_jogo')
    id_campeonato = models.ForeignKey(Campeonatos, models.DO_NOTHING, db_column='id_campeonato')
    id_equipa = models.ForeignKey('Equipas', models.DO_NOTHING, db_column='id_equipa')
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campeonatos_jogos_equipas'


class Clube(models.Model):
    id_clube = models.AutoField(primary_key=True)
    nome = models.TextField()
    endereco = models.TextField()
    telefone = models.IntegerField()
    presidente = models.TextField()
    distrito = models.TextField()
    email = models.TextField()
    status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'clube'


class Epocas(models.Model):
    id_epoca = models.AutoField(primary_key=True)
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'epocas'


class Equipas(models.Model):
    id_equipa = models.AutoField(primary_key=True)
    id_genero = models.ForeignKey('Generos', models.DO_NOTHING, db_column='id_genero')
    id_clube = models.ForeignKey(Clube, models.DO_NOTHING, db_column='id_clube')
    id_modalidade = models.ForeignKey('Modalidades', models.DO_NOTHING, db_column='id_modalidade')
    id_faixa_etaria = models.ForeignKey('FaixaEtaria', models.DO_NOTHING, db_column='id_faixa_etaria')
    equipa = models.TextField()
    treinador = models.TextField()
    sede = models.TextField(blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipas'


class FaixaEtaria(models.Model):
    id_faixa_etaria = models.AutoField(primary_key=True)
    faixa_etaria = models.TextField()
    idade_inicio = models.IntegerField(blank=True, null=True)
    idade_fim = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.faixa_etaria

    class Meta:
        managed = False
        db_table = 'faixa_etaria'


class Generos(models.Model):
    id_genero = models.AutoField(primary_key=True)
    genero = models.TextField()
    status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.genero

    class Meta:
        managed = False
        db_table = 'generos'


class Jogadores(models.Model):
    id_jogador = models.AutoField(primary_key=True)
    nome = models.TextField()
    data_nascimento = models.DateField()
    telemovel = models.IntegerField()
    altura = models.IntegerField()
    naturalidade = models.TextField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogadores'


class JogadoresJogosEquipas(models.Model):
    id_equipa = models.ForeignKey(Equipas, models.DO_NOTHING, db_column='id_equipa')
    id_jogo = models.ForeignKey('Jogos', models.DO_NOTHING, db_column='id_jogo')
    id_jogador = models.ForeignKey(Jogadores, models.DO_NOTHING, db_column='id_jogador')
    titular = models.BooleanField()
    numero_jogador = models.IntegerField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogadores_jogos_equipas'


class Jogam(models.Model):
    id_jogador = models.ForeignKey(Jogadores, models.DO_NOTHING, db_column='id_jogador', primary_key=True)
    id_equipa = models.ForeignKey(Equipas, models.DO_NOTHING, db_column='id_equipa')
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogam'
        unique_together = (('id_jogador', 'id_equipa'), ('id_jogador', 'id_equipa'),)


class Jogos(models.Model):
    id_jogo = models.AutoField(primary_key=True)
    data_hora = models.DateField()
    local = models.TextField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogos'


class JogosJogadoresAcoesdiscip(models.Model):
    id_jogo = models.ForeignKey(Jogos, models.DO_NOTHING, db_column='id_jogo')
    id_jogador = models.ForeignKey(Jogadores, models.DO_NOTHING, db_column='id_jogador')
    id_acao_disciplinar = models.ForeignKey(AcoesDisciplinares, models.DO_NOTHING, db_column='id_acao_disciplinar')
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogos_jogadores_acoesdiscip'


class Modalidades(models.Model):
    id_modalidade = models.AutoField(primary_key=True)
    modalidade = models.TextField()
    status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.modalidade

    class Meta:
        managed = False
        db_table = 'modalidades'


class Pontuacoes(models.Model):
    id_pontuacao = models.AutoField(primary_key=True)
    id_tipo_pontuacao = models.ForeignKey('TipoPontuacao', models.DO_NOTHING, db_column='id_tipo_pontuacao')
    pontuacao = models.TextField()
    tempo_jogo = models.CharField(max_length=256)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pontuacoes'


class PontuacoesJogadoresJogos(models.Model):
    id_pontuacao = models.ForeignKey(Pontuacoes, models.DO_NOTHING, db_column='id_pontuacao')
    id_jogador = models.ForeignKey(Jogadores, models.DO_NOTHING, db_column='id_jogador')
    id_jogo = models.ForeignKey(Jogos, models.DO_NOTHING, db_column='id_jogo')
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pontuacoes_jogadores_jogos'


class Substituicoes(models.Model):
    id_sub = models.AutoField(primary_key=True)
    id_jogador = models.ForeignKey(Jogadores, models.DO_NOTHING, db_column='id_jogador')
    id_jogo = models.ForeignKey(Jogos, models.DO_NOTHING, db_column='id_jogo')
    tempo_jogo = models.TextField()
    entra = models.BooleanField()
    sai = models.BooleanField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'substituicoes'


class TipoAcaoDisciplinar(models.Model):
    id_tipo_acao_disciplinar = models.AutoField(primary_key=True)
    acao_disciplinar = models.TextField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_acao_disciplinar'


class TipoPontuacao(models.Model):
    id_tipo_pontuacao = models.AutoField(primary_key=True)
    tipo_pontuacao = models.TextField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_pontuacao'
