# Generated by Django 2.2.16 on 2021-02-06 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcoesDisciplinares',
            fields=[
                ('id_acao_disciplinar', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('tempo_jogo', models.CharField(max_length=256)),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'acoes_disciplinares',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Campeonatos',
            fields=[
                ('id_campeonato', models.AutoField(primary_key=True, serialize=False)),
                ('nome_campeonato', models.TextField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'campeonatos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id_clube', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('endereco', models.TextField()),
                ('telefone', models.IntegerField()),
                ('presidente', models.TextField()),
                ('distrito', models.TextField()),
                ('email', models.TextField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'clube',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Epocas',
            fields=[
                ('id_epoca', models.AutoField(primary_key=True, serialize=False)),
                ('ano_inicio', models.IntegerField()),
                ('ano_fim', models.IntegerField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'epocas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Equipas',
            fields=[
                ('id_equipa', models.AutoField(primary_key=True, serialize=False)),
                ('equipa', models.TextField()),
                ('treinador', models.TextField()),
                ('sede', models.TextField(blank=True, null=True)),
                ('telefone', models.IntegerField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
                ('id_clube', models.ForeignKey(db_column='id_clube', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Clube')),
            ],
            options={
                'db_table': 'equipas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FaixaEtaria',
            fields=[
                ('id_faixa_etaria', models.AutoField(primary_key=True, serialize=False)),
                ('faixa_etaria', models.TextField()),
                ('idade_inicio', models.IntegerField(blank=True, null=True)),
                ('idade_fim', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'faixa_etaria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.TextField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'generos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Jogadores',
            fields=[
                ('id_jogador', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('data_nascimento', models.DateField()),
                ('telemovel', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('naturalidade', models.TextField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'jogadores',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id_jogo', models.AutoField(primary_key=True, serialize=False)),
                ('data_hora', models.DateField()),
                ('local', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'jogos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Modalidades',
            fields=[
                ('id_modalidade', models.AutoField(primary_key=True, serialize=False)),
                ('modalidade', models.TextField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'modalidades',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pontuacoes',
            fields=[
                ('id_pontuacao', models.AutoField(primary_key=True, serialize=False)),
                ('pontuacao', models.TextField()),
                ('tempo_jogo', models.CharField(max_length=256)),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'pontuacoes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoAcaoDisciplinar',
            fields=[
                ('id_tipo_acao_disciplinar', models.AutoField(primary_key=True, serialize=False)),
                ('acao_disciplinar', models.TextField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'tipo_acao_disciplinar',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoPontuacao',
            fields=[
                ('id_tipo_pontuacao', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_pontuacao', models.TextField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
            ],
            options={
                'db_table': 'tipo_pontuacao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Substituicoes',
            fields=[
                ('id_sub', models.AutoField(primary_key=True, serialize=False)),
                ('tempo_jogo', models.TextField()),
                ('entra', models.BooleanField()),
                ('sai', models.BooleanField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
                ('id_jogador', models.ForeignKey(db_column='id_jogador', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogadores')),
                ('id_jogo', models.ForeignKey(db_column='id_jogo', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogos')),
            ],
            options={
                'db_table': 'substituicoes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PontuacoesJogadoresJogos',
            fields=[
                ('id_pontuacoes_jogadores_jogos', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
                ('id_jogador', models.ForeignKey(db_column='id_jogador', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogadores')),
                ('id_jogo', models.ForeignKey(db_column='id_jogo', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogos')),
                ('id_pontuacao', models.ForeignKey(db_column='id_pontuacao', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Pontuacoes')),
            ],
            options={
                'db_table': 'pontuacoes_jogadores_jogos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='pontuacoes',
            name='id_tipo_pontuacao',
            field=models.ForeignKey(db_column='id_tipo_pontuacao', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.TipoPontuacao'),
        ),
        migrations.CreateModel(
            name='JogosJogadoresAcoesdiscip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
                ('id_acao_disciplinar', models.ForeignKey(db_column='id_acao_disciplinar', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.AcoesDisciplinares')),
                ('id_jogador', models.ForeignKey(db_column='id_jogador', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogadores')),
                ('id_jogo', models.ForeignKey(db_column='id_jogo', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogos')),
            ],
            options={
                'db_table': 'jogos_jogadores_acoesdiscip',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='JogadoresJogosEquipas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.BooleanField()),
                ('numero_jogador', models.IntegerField()),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
                ('id_equipa', models.ForeignKey(db_column='id_equipa', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Equipas')),
                ('id_jogador', models.ForeignKey(db_column='id_jogador', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogadores')),
                ('id_jogo', models.ForeignKey(db_column='id_jogo', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogos')),
            ],
            options={
                'db_table': 'jogadores_jogos_equipas',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='equipas',
            name='id_faixa_etaria',
            field=models.ForeignKey(db_column='id_faixa_etaria', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.FaixaEtaria'),
        ),
        migrations.AddField(
            model_name='equipas',
            name='id_genero',
            field=models.ForeignKey(db_column='id_genero', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Generos'),
        ),
        migrations.AddField(
            model_name='equipas',
            name='id_modalidade',
            field=models.ForeignKey(db_column='id_modalidade', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Modalidades'),
        ),
        migrations.CreateModel(
            name='CampeonatosJogosEquipas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
                ('id_campeonato', models.ForeignKey(db_column='id_campeonato', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Campeonatos')),
                ('id_equipa', models.ForeignKey(db_column='id_equipa', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Equipas')),
                ('id_jogo', models.ForeignKey(db_column='id_jogo', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Jogos')),
            ],
            options={
                'db_table': 'campeonatos_jogos_equipas',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='campeonatos',
            name='id_epoca',
            field=models.ForeignKey(db_column='id_epoca', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Epocas'),
        ),
        migrations.AddField(
            model_name='campeonatos',
            name='id_modalidade',
            field=models.ForeignKey(db_column='id_modalidade', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Modalidades'),
        ),
        migrations.AddField(
            model_name='acoesdisciplinares',
            name='id_tipo_acao_disciplinar',
            field=models.ForeignKey(db_column='id_tipo_acao_disciplinar', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.TipoAcaoDisciplinar'),
        ),
        migrations.CreateModel(
            name='Jogam',
            fields=[
                ('id_jogador', models.ForeignKey(db_column='id_jogador', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='django_bd2_pagina.Jogadores')),
                ('status', models.BooleanField(blank=True, default='True', null=True)),
                ('id_equipa', models.ForeignKey(db_column='id_equipa', on_delete=django.db.models.deletion.DO_NOTHING, to='django_bd2_pagina.Equipas')),
            ],
            options={
                'db_table': 'jogam',
                'managed': True,
                'unique_together': {('id_jogador', 'id_equipa')},
            },
        ),
    ]
