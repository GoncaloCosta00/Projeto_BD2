/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     09/12/2020 09:54:52                          */
/*==============================================================*/

/*
drop index ASSOCIADO_FK;

drop index ACOES_DISCIPLINARES_PK;

drop table ACOES_DISCIPLINARES;

drop index INTEGRADO_FK;

drop index DISPUTADO_FK;

drop index CAMPEONATOS_PK;

drop table CAMPEONATOS;

drop index PERTENCEM_FK;

drop index DISPUTA_FK;

drop index INTEGRA_FK;

drop table campeonatos_jogos_equipas;

drop index CLUBE_PK;

drop table CLUBE;

drop index EPOCAS_PK;

drop table EPOCAS;

drop index COMPOSTO_FK;

drop index PRATICA_FK;

drop index PERTENCE_FK;

drop index RELATIONSHIP_1_FK;

drop index EQUIPAS_PK;

drop table EQUIPAS;

drop index FAIXA_ETARIA_PK;

drop table FAIXA_ETARIA;

drop index GENEROS_PK;

drop table GENEROS;

drop index JOGADORES_PK;

drop table JOGADORES;

drop index CONTEM_FK;

drop index DISPUTAM_FK;

drop index REALIZA_FK;

drop table JOGADORES_JOGOS_EQUIPAS;

drop index JOGAM2_FK;

drop index JOGAM_FK;

drop index JOGAM_PK;

drop table JOGAM;

drop index JOGOS_PK;

drop table JOGOS;

drop index ATRIBUIDAS_FK;

drop index SELECIONADOS_FK;

drop index POSSUI_FK;

drop table JOGOS_JOGADORES_ACOESDISCIP;

drop index MODALIDADES_PK;

drop table MODALIDADES;

drop index ENGLOBADO_FK;

drop index PONTUACOES_PK;

drop table PONTUACOES;

drop index REGISTADO_FK;

drop index ENGLOBA_FK;

drop index REFERENTE_FK;

drop table pontuacoes_jogadores_jogos;

drop index OCORREM_FK;

drop index EFETUA_FK;

drop index SUBSTITUICOES_PK;

drop table SUBSTITUICOES;

drop index TIPO_ACAO_DISCIPLINAR_PK;

drop table TIPO_ACAO_DISCIPLINAR;

drop index TIPO_PONTUACAO_PK;

drop table TIPO_PONTUACAO;
*/
/*==============================================================*/
/* Table: ACOES_DISCIPLINARES                                   */
/*==============================================================*/

create sequence sequencia;

create table ACOES_DISCIPLINARES (
   ID_ACAO_DISCIPLINAR  SERIAL               not null,
   ID_TIPO_ACAO_DISCIPLINAR INT4                 not null,
   COMENTARIO           TEXT                 null default "acaodisciplinar"||nextval("sequencia"),
   TEMPO_JOGO           CHAR(256)            not null,
   status 				boolean 			default true,
   constraint PK_ACOES_DISCIPLINARES primary key (ID_ACAO_DISCIPLINAR)
);

/*==============================================================*/
/* Index: ACOES_DISCIPLINARES_PK                                */
/*==============================================================*/
create unique index ACOES_DISCIPLINARES_PK on ACOES_DISCIPLINARES (
ID_ACAO_DISCIPLINAR
);

/*==============================================================*/
/* Index: ASSOCIADO_FK                                          */
/*==============================================================*/
create  index ASSOCIADO_FK on ACOES_DISCIPLINARES (
ID_TIPO_ACAO_DISCIPLINAR
);

/*==============================================================*/
/* Table: CAMPEONATOS                                           */
/*==============================================================*/
create table CAMPEONATOS (
   ID_CAMPEONATO        SERIAL               not null,
   ID_MODALIDADE        INT4                 not null,
   ID_EPOCA             INT4                 not null,
   NOME_CAMPEONATO      TEXT                 not null,
   status 				boolean 			default true,
   constraint PK_CAMPEONATOS primary key (ID_CAMPEONATO)
);

/*==============================================================*/
/* Index: CAMPEONATOS_PK                                        */
/*==============================================================*/
create unique index CAMPEONATOS_PK on CAMPEONATOS (
ID_CAMPEONATO
);

/*==============================================================*/
/* Index: DISPUTADO_FK                                          */
/*==============================================================*/
create  index DISPUTADO_FK on CAMPEONATOS (
ID_EPOCA
);

/*==============================================================*/
/* Index: INTEGRADO_FK                                          */
/*==============================================================*/
create  index INTEGRADO_FK on CAMPEONATOS (
ID_MODALIDADE
);

/*==============================================================*/
/* Table: campeonatos_jogos_equipas                         */
/*==============================================================*/
create table campeonatos_jogos_equipas (
   ID_JOGO              INT4                 not null,
   ID_CAMPEONATO        INT4                 not null,
   ID_EQUIPA            INT4                 not null,
   status 				boolean 			default true
);

/*==============================================================*/
/* Index: INTEGRA_FK                                            */
/*==============================================================*/
create  index INTEGRA_FK on campeonatos_jogos_equipas (
ID_CAMPEONATO
);

/*==============================================================*/
/* Index: DISPUTA_FK                                            */
/*==============================================================*/
create  index DISPUTA_FK on campeonatos_jogos_equipas (
ID_EQUIPA
);

/*==============================================================*/
/* Index: PERTENCEM_FK                                          */
/*==============================================================*/
create  index PERTENCEM_FK on campeonatos_jogos_equipas (
ID_JOGO
);

/*==============================================================*/
/* Table: CLUBE                                                 */
/*==============================================================*/
create table CLUBE (
   ID_CLUBE             SERIAL               not null,
   NOME                 TEXT                 not null,
   ENDERECO             TEXT                 not null,
   TELEFONE             INT4                 not null,
   PRESIDENTE           TEXT                 not null,
   DISTRITO             TEXT                 not null,
   EMAIL                TEXT                 not null,
   status 				boolean 			default true,
   constraint PK_CLUBE primary key (ID_CLUBE)
);

/*==============================================================*/
/* Index: CLUBE_PK                                              */
/*==============================================================*/
create unique index CLUBE_PK on CLUBE (
ID_CLUBE
);

/*==============================================================*/
/* Table: EPOCAS                                                */
/*==============================================================*/
create table EPOCAS (
   ID_EPOCA             SERIAL               not null,
   ANO_INICIO           INT4                 not null,
   ANO_FIM              INT4                 not null,
   status 				boolean 			default true,
   constraint PK_EPOCAS primary key (ID_EPOCA)
);

/*==============================================================*/
/* Index: EPOCAS_PK                                             */
/*==============================================================*/
create unique index EPOCAS_PK on EPOCAS (
ID_EPOCA
);

/*==============================================================*/
/* Table: EQUIPAS                                               */
/*==============================================================*/
create table EQUIPAS (
   ID_EQUIPA            SERIAL               not null,
   ID_GENERO            INT4                 not null,
   ID_CLUBE             INT4                 not null,
   ID_MODALIDADE        INT4                 not null,
   ID_FAIXA_ETARIA      INT4                 not null,
   EQUIPA               TEXT                 not null,
   TREINADOR            TEXT                 not null,
   SEDE                 TEXT                 null,
   TELEFONE             INT4                 null,
   EMAIL                TEXT                 null,
   status 				boolean 			default true,
   constraint PK_EQUIPAS primary key (ID_EQUIPA)
);

/*==============================================================*/
/* Index: EQUIPAS_PK                                            */
/*==============================================================*/
create unique index EQUIPAS_PK on EQUIPAS (
ID_EQUIPA
);

/*==============================================================*/
/* Index: RELATIONSHIP_1_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_1_FK on EQUIPAS (
ID_GENERO
);

/*==============================================================*/
/* Index: PERTENCE_FK                                           */
/*==============================================================*/
create  index PERTENCE_FK on EQUIPAS (
ID_FAIXA_ETARIA
);

/*==============================================================*/
/* Index: PRATICA_FK                                            */
/*==============================================================*/
create  index PRATICA_FK on EQUIPAS (
ID_MODALIDADE
);

/*==============================================================*/
/* Index: COMPOSTO_FK                                           */
/*==============================================================*/
create  index COMPOSTO_FK on EQUIPAS (
ID_CLUBE
);

/*==============================================================*/
/* Table: FAIXA_ETARIA                                          */
/*==============================================================*/
create table FAIXA_ETARIA (
   ID_FAIXA_ETARIA      SERIAL               not null,
   FAIXA_ETARIA         TEXT                 not null,
   IDADE_INICIO         INT4                 null,
   IDADE_FIM            INT4                 null,
   status 				boolean 			default true,
   constraint PK_FAIXA_ETARIA primary key (ID_FAIXA_ETARIA)
);

/*==============================================================*/
/* Index: FAIXA_ETARIA_PK                                       */
/*==============================================================*/
create unique index FAIXA_ETARIA_PK on FAIXA_ETARIA (
ID_FAIXA_ETARIA
);

/*==============================================================*/
/* Table: GENEROS                                               */
/*==============================================================*/
create table GENEROS (
   ID_GENERO            SERIAL               not null,
   GENERO               TEXT                 not null,
   status 				boolean 			default true,
   constraint PK_GENEROS primary key (ID_GENERO)
);

/*==============================================================*/
/* Index: GENEROS_PK                                            */
/*==============================================================*/
create unique index GENEROS_PK on GENEROS (
ID_GENERO
);

/*==============================================================*/
/* Table: JOGADORES                                             */
/*==============================================================*/
create table JOGADORES (
   ID_JOGADOR           SERIAL               not null,
   NOME                 TEXT                 not null,
   DATA_NASCIMENTO      DATE                 not null,
   TELEMOVEL            INT4                 not null,
   ALTURA               INT4                 not null,
   NATURALIDADE         TEXT                 not null,
   status 				boolean 			default true,
   constraint PK_JOGADORES primary key (ID_JOGADOR)
);

/*==============================================================*/
/* Index: JOGADORES_PK                                          */
/*==============================================================*/
create unique index JOGADORES_PK on JOGADORES (
ID_JOGADOR
);

/*==============================================================*/
/* Table: JOGADORES_JOGOS_EQUIPAS                               */
/*==============================================================*/
create table JOGADORES_JOGOS_EQUIPAS (
   ID_EQUIPA            INT4                 not null,
   ID_JOGO              INT4                 not null,
   ID_JOGADOR           INT4                 not null,
   TITULAR              BOOL                 not null,
   NUMERO_JOGADOR       INT4                 not null,
   status 				boolean 			default true
);

/*==============================================================*/
/* Index: REALIZA_FK                                            */
/*==============================================================*/
create  index REALIZA_FK on JOGADORES_JOGOS_EQUIPAS (
ID_JOGADOR
);

/*==============================================================*/
/* Index: DISPUTAM_FK                                           */
/*==============================================================*/
create  index DISPUTAM_FK on JOGADORES_JOGOS_EQUIPAS (
ID_JOGO
);

/*==============================================================*/
/* Index: CONTEM_FK                                             */
/*==============================================================*/
create  index CONTEM_FK on JOGADORES_JOGOS_EQUIPAS (
ID_EQUIPA
);

/*==============================================================*/
/* Table: JOGAM                                                 */
/*==============================================================*/
create table JOGAM (
   ID_JOGADOR           INT4                 not null,
   ID_EQUIPA            INT4                 not null,
   status 				boolean 			default true,
   constraint PK_JOGAM primary key (ID_JOGADOR, ID_EQUIPA)
);

/*==============================================================*/
/* Index: JOGAM_PK                                              */
/*==============================================================*/
create unique index JOGAM_PK on JOGAM (
ID_JOGADOR,
ID_EQUIPA
);

/*==============================================================*/
/* Index: JOGAM_FK                                              */
/*==============================================================*/
create  index JOGAM_FK on JOGAM (
ID_JOGADOR
);

/*==============================================================*/
/* Index: JOGAM2_FK                                             */
/*==============================================================*/
create  index JOGAM2_FK on JOGAM (
ID_EQUIPA
);

/*==============================================================*/
/* Table: JOGOS                                                 */
/*==============================================================*/
create table JOGOS (
   ID_JOGO              SERIAL               not null,
   DATA_HORA            DATE                 not null,
   LOCAL                TEXT                 null,
   status 				boolean 			default true,
   constraint PK_JOGOS primary key (ID_JOGO)
);

/*==============================================================*/
/* Index: JOGOS_PK                                              */
/*==============================================================*/
create unique index JOGOS_PK on JOGOS (
ID_JOGO
);

/*==============================================================*/
/* Table: JOGOS_JOGADORES_ACOESDISCIP                           */
/*==============================================================*/
create table JOGOS_JOGADORES_ACOESDISCIP (
   ID_JOGO              INT4                 not null,
   ID_JOGADOR           INT4                 not null,
   ID_ACAO_DISCIPLINAR  INT4                 not null,
   status 				boolean 			default true
);

/*==============================================================*/
/* Index: POSSUI_FK                                             */
/*==============================================================*/
create  index POSSUI_FK on JOGOS_JOGADORES_ACOESDISCIP (
ID_JOGO
);

/*==============================================================*/
/* Index: SELECIONADOS_FK                                       */
/*==============================================================*/
create  index SELECIONADOS_FK on JOGOS_JOGADORES_ACOESDISCIP (
ID_JOGADOR
);

/*==============================================================*/
/* Index: ATRIBUIDAS_FK                                         */
/*==============================================================*/
create  index ATRIBUIDAS_FK on JOGOS_JOGADORES_ACOESDISCIP (
ID_ACAO_DISCIPLINAR
);

/*==============================================================*/
/* Table: MODALIDADES                                           */
/*==============================================================*/
create table MODALIDADES (
   ID_MODALIDADE        SERIAL               not null,
   MODALIDADE           TEXT                 not null,
   status 				boolean 			default true,
   constraint PK_MODALIDADES primary key (ID_MODALIDADE)
);

/*==============================================================*/
/* Index: MODALIDADES_PK                                        */
/*==============================================================*/
create unique index MODALIDADES_PK on MODALIDADES (
ID_MODALIDADE
);

/*==============================================================*/
/* Table: PONTUACOES                                            */
/*==============================================================*/
create table PONTUACOES (
   ID_PONTUACAO         SERIAL               not null,
   ID_TIPO_PONTUACAO    INT4                 not null,
   PONTUACAO            TEXT                 not null,
   TEMPO_JOGO           CHAR(256)            not null,
   status 				boolean 			default true,
   constraint PK_PONTUACOES primary key (ID_PONTUACAO)
);

/*==============================================================*/
/* Index: PONTUACOES_PK                                         */
/*==============================================================*/
create unique index PONTUACOES_PK on PONTUACOES (
ID_PONTUACAO
);

/*==============================================================*/
/* Index: ENGLOBADO_FK                                          */
/*==============================================================*/
create  index ENGLOBADO_FK on PONTUACOES (
ID_TIPO_PONTUACAO
);

/*==============================================================*/
/* Table: pontuacoes_jogadores_jogos                          */
/*==============================================================*/
create table pontuacoes_jogadores_jogos (
   ID_PONTUACAO         INT4                 not null,
   ID_JOGADOR           INT4                 not null,
   ID_JOGO              INT4                 not null,
   status 				boolean 			default true
);

/*==============================================================*/
/* Index: REFERENTE_FK                                          */
/*==============================================================*/
create  index REFERENTE_FK on pontuacoes_jogadores_jogos (
ID_PONTUACAO
);

/*==============================================================*/
/* Index: ENGLOBA_FK                                            */
/*==============================================================*/
create  index ENGLOBA_FK on pontuacoes_jogadores_jogos (
ID_JOGO
);

/*==============================================================*/
/* Index: REGISTADO_FK                                          */
/*==============================================================*/
create  index REGISTADO_FK on pontuacoes_jogadores_jogos (
ID_JOGADOR
);

/*==============================================================*/
/* Table: SUBSTITUICOES                                         */
/*==============================================================*/
create table SUBSTITUICOES (
   ID_SUB               SERIAL               not null,
   ID_JOGADOR           INT4                 not null,
   ID_JOGO              INT4                 not null,
   TEMPO_JOGO           TEXT                 not null,
   ENTRA                bool                 not null,
   SAI                  bool                 not null,
   status 				boolean 			default true,
   constraint PK_SUBSTITUICOES primary key (ID_SUB)
);

/*==============================================================*/
/* Index: SUBSTITUICOES_PK                                      */
/*==============================================================*/
create unique index SUBSTITUICOES_PK on SUBSTITUICOES (
ID_SUB
);

/*==============================================================*/
/* Index: EFETUA_FK                                             */
/*==============================================================*/
create  index EFETUA_FK on SUBSTITUICOES (
ID_JOGADOR
);

/*==============================================================*/
/* Index: OCORREM_FK                                            */
/*==============================================================*/
create  index OCORREM_FK on SUBSTITUICOES (
ID_JOGO
);

/*==============================================================*/
/* Table: TIPO_ACAO_DISCIPLINAR                                 */
/*==============================================================*/
create table TIPO_ACAO_DISCIPLINAR (
   ID_TIPO_ACAO_DISCIPLINAR SERIAL               not null,
   ACAO_DISCIPLINAR     TEXT                 not null,
   status 				boolean 			default true,
   constraint PK_TIPO_ACAO_DISCIPLINAR primary key (ID_TIPO_ACAO_DISCIPLINAR)
);

/*==============================================================*/
/* Index: TIPO_ACAO_DISCIPLINAR_PK                              */
/*==============================================================*/
create unique index TIPO_ACAO_DISCIPLINAR_PK on TIPO_ACAO_DISCIPLINAR (
ID_TIPO_ACAO_DISCIPLINAR
);

/*==============================================================*/
/* Table: TIPO_PONTUACAO                                        */
/*==============================================================*/
create table TIPO_PONTUACAO (
   ID_TIPO_PONTUACAO    SERIAL               not null,
   TIPO_PONTUACAO       TEXT                 not null,
   status 				boolean 			default true,
   constraint PK_TIPO_PONTUACAO primary key (ID_TIPO_PONTUACAO)
);

/*==============================================================*/
/* Index: TIPO_PONTUACAO_PK                                     */
/*==============================================================*/
create unique index TIPO_PONTUACAO_PK on TIPO_PONTUACAO (
ID_TIPO_PONTUACAO
);

alter table ACOES_DISCIPLINARES
   add constraint FK_ACOES_DI_ASSOCIADO_TIPO_ACA foreign key (ID_TIPO_ACAO_DISCIPLINAR)
      references TIPO_ACAO_DISCIPLINAR (ID_TIPO_ACAO_DISCIPLINAR)
      on delete restrict on update restrict;

alter table CAMPEONATOS
   add constraint FK_CAMPEONA_DISPUTADO_EPOCAS foreign key (ID_EPOCA)
      references EPOCAS (ID_EPOCA)
      on delete restrict on update restrict;

alter table CAMPEONATOS
   add constraint FK_CAMPEONA_INTEGRADO_MODALIDA foreign key (ID_MODALIDADE)
      references MODALIDADES (ID_MODALIDADE)
      on delete restrict on update restrict;

alter table campeonatos_jogos_equipas
   add constraint FK_CAMPEONA_DISPUTA_EQUIPAS foreign key (ID_EQUIPA)
      references EQUIPAS (ID_EQUIPA)
      on delete restrict on update restrict;

alter table campeonatos_jogos_equipas
   add constraint FK_CAMPEONA_INTEGRA_CAMPEONA foreign key (ID_CAMPEONATO)
      references CAMPEONATOS (ID_CAMPEONATO)
      on delete restrict on update restrict;

alter table campeonatos_jogos_equipas
   add constraint FK_CAMPEONA_PERTENCEM_JOGOS foreign key (ID_JOGO)
      references JOGOS (ID_JOGO)
      on delete restrict on update restrict;

alter table EQUIPAS
   add constraint FK_EQUIPAS_COMPOSTO_CLUBE foreign key (ID_CLUBE)
      references CLUBE (ID_CLUBE)
      on delete restrict on update restrict;

alter table EQUIPAS
   add constraint FK_EQUIPAS_PERTENCE_FAIXA_ET foreign key (ID_FAIXA_ETARIA)
      references FAIXA_ETARIA (ID_FAIXA_ETARIA)
      on delete restrict on update restrict;

alter table EQUIPAS
   add constraint FK_EQUIPAS_PRATICA_MODALIDA foreign key (ID_MODALIDADE)
      references MODALIDADES (ID_MODALIDADE)
      on delete restrict on update restrict;

alter table EQUIPAS
   add constraint FK_EQUIPAS_RELATIONS_GENEROS foreign key (ID_GENERO)
      references GENEROS (ID_GENERO)
      on delete restrict on update restrict;

alter table JOGADORES_JOGOS_EQUIPAS
   add constraint FK_JOGADORE_CONTEM_EQUIPAS foreign key (ID_EQUIPA)
      references EQUIPAS (ID_EQUIPA)
      on delete restrict on update restrict;

alter table JOGADORES_JOGOS_EQUIPAS
   add constraint FK_JOGADORE_DISPUTAM_JOGOS foreign key (ID_JOGO)
      references JOGOS (ID_JOGO)
      on delete restrict on update restrict;

alter table JOGADORES_JOGOS_EQUIPAS
   add constraint FK_JOGADORE_REALIZA_JOGADORE foreign key (ID_JOGADOR)
      references JOGADORES (ID_JOGADOR)
      on delete restrict on update restrict;

alter table JOGAM
   add constraint FK_JOGAM_JOGAM_JOGADORE foreign key (ID_JOGADOR)
      references JOGADORES (ID_JOGADOR)
      on delete restrict on update restrict;

alter table JOGAM
   add constraint FK_JOGAM_JOGAM2_EQUIPAS foreign key (ID_EQUIPA)
      references EQUIPAS (ID_EQUIPA)
      on delete restrict on update restrict;

alter table JOGOS_JOGADORES_ACOESDISCIP
   add constraint FK_JOGOS_JO_ATRIBUIDA_ACOES_DI foreign key (ID_ACAO_DISCIPLINAR)
      references ACOES_DISCIPLINARES (ID_ACAO_DISCIPLINAR)
      on delete restrict on update restrict;

alter table JOGOS_JOGADORES_ACOESDISCIP
   add constraint FK_JOGOS_JO_POSSUI_JOGOS foreign key (ID_JOGO)
      references JOGOS (ID_JOGO)
      on delete restrict on update restrict;

alter table JOGOS_JOGADORES_ACOESDISCIP
   add constraint FK_JOGOS_JO_SELECIONA_JOGADORE foreign key (ID_JOGADOR)
      references JOGADORES (ID_JOGADOR)
      on delete restrict on update restrict;

alter table PONTUACOES
   add constraint FK_PONTUACO_ENGLOBADO_TIPO_PON foreign key (ID_TIPO_PONTUACAO)
      references TIPO_PONTUACAO (ID_TIPO_PONTUACAO)
      on delete restrict on update restrict;

alter table pontuacoes_jogadores_jogos
   add constraint FK_PONTUACO_ENGLOBA_JOGOS foreign key (ID_JOGO)
      references JOGOS (ID_JOGO)
      on delete restrict on update restrict;

alter table pontuacoes_jogadores_jogos
   add constraint FK_PONTUACO_REFERENTE_PONTUACO foreign key (ID_PONTUACAO)
      references PONTUACOES (ID_PONTUACAO)
      on delete restrict on update restrict;

alter table pontuacoes_jogadores_jogos
   add constraint FK_PONTUACO_REGISTADO_JOGADORE foreign key (ID_JOGADOR)
      references JOGADORES (ID_JOGADOR)
      on delete restrict on update restrict;

alter table SUBSTITUICOES
   add constraint FK_SUBSTITU_EFETUA_JOGADORE foreign key (ID_JOGADOR)
      references JOGADORES (ID_JOGADOR)
      on delete restrict on update restrict;

alter table SUBSTITUICOES
   add constraint FK_SUBSTITU_OCORREM_JOGOS foreign key (ID_JOGO)
      references JOGOS (ID_JOGO)
      on delete restrict on update restrict;

