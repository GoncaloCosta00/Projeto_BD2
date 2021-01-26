--drop function calcular_golos_equipa() if exists;
create or replace function calcular_golos_equipa(equipa int, campeonato int)
returns int 
language plpgsql
as $$
begin
	return( select count(*) from (select * from pontuacoes_jogadores_jogos join campeonatos_jogos_equipas
on pontuacoes_jogadores_jogos.id_jogo = campeonatos_jogos_equipas.id_jogo
where campeonatos_jogos_equipas.id_equipa = equipa and campeonatos_jogos_equipas.id_campeonato = campeonato and pontuacoes_jogadores_jogos.status = 'true'and campeonatos_jogos_equipas.status = 'true') as golos_da_equipa);
	
end;
$$


--drop function calcular_golos_jogador() if exists;
create or replace function calcular_golos_jogador(jogador int, campeonato int)
returns int 
language plpgsql
as $$
begin
	return( select count(*) from (select * from pontuacoes_jogadores_jogos join campeonatos_jogos_equipas
on pontuacoes_jogadores_jogos.id_jogo = campeonatos_jogos_equipas.id_jogo
where pontuacoes_jogadores_jogos.id_jogador = jogador and campeonatos_jogos_equipas.id_campeonato = campeonato and pontuacoes_jogadores_jogos.status = 'true'and campeonatos_jogos_equipas.status = 'true') as golos_da_equipa);
	
end;
$$


