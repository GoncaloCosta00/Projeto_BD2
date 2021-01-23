--drop function calcular_golos_equipa() if exists;
create or replace function calcular_golos_equipa(jogador int, campeonato int)
returns int 
language plpgsql
as $$
begin
	return( select count(*) from (select jogadores_jogos_equipas.id_jogo, campeonatos___jogos___equipas.id_equipa,jogadores_jogos_equipas.id_equipa, campeonatos___jogos___equipas.id_campeonato, pontuacoes___jogadores_jogos.status from pontuacoes___jogadores_jogos  join jogadores_jogos_equipas 
	on pontuacoes___jogadores_jogos.id_jogo = jogadores_jogos_equipas.id_jogo join campeonatos___jogos___equipas
	on campeonatos___jogos___equipas.id_equipa = jogadores_jogos_equipas.id_equipa
	group by pontuacoes___jogadores_jogos.id_jogo, jogadores_jogos_equipas.id_jogo, campeonatos___jogos___equipas.id_equipa,jogadores_jogos_equipas.id_equipa, campeonatos___jogos___equipas.id_campeonato, pontuacoes___jogadores_jogos.status 
	having jogadores_jogos_equipas.id_equipa = equipa and campeonatos___jogos___equipas.id_campeonato = campeonato and pontuacoes___jogadores_jogos.status = 'true') as golos_da_equipa);
	
end;
$$


--drop function calcular_golos_jogador() if exists;
create or replace function calcular_golos_jogador(jogador int, campeonato int)
returns int 
language plpgsql
as $$
begin
	return (select count(*) from (select pontuacoes___jogadores_jogos.id_jogador, jogadores_jogos_equipas.id_jogador, jogadores_jogos_equipas.id_jogo,campeonatos___jogos___equipas.id_campeonato, pontuacoes___jogadores_jogos .status from pontuacoes___jogadores_jogos  inner join jogadores_jogos_equipas 
	on pontuacoes___jogadores_jogos.id_jogo = jogadores_jogos_equipas.id_jogo inner join campeonatos___jogos___equipas
	on campeonatos___jogos___equipas.id_jogo = jogadores_jogos_equipas.id_jogo
	group by pontuacoes___jogadores_jogos.id_jogador,jogadores_jogos_equipas.id_jogador, jogadores_jogos_equipas.id_jogo,pontuacoes___jogadores_jogos.id_pontuacao, pontuacoes___jogadores_jogos.id_jogo, pontuacoes___jogadores_jogos.status, campeonatos___jogos___equipas.id_campeonato
	having pontuacoes___jogadores_jogos.id_jogador = jogador and jogadores_jogos_equipas.id_jogador = jogador and campeonatos___jogos___equipas.id_campeonato = campeonato and pontuacoes___jogadores_jogos .status = 'true') as golos);
end;
$$


