create or replace function calcular_minutos_jogador(jogador int, campeonato int)
returns int 
language plpgsql
as $$
declare 
minutos_substituicao_sai int;
minutos_substituicao_entra int;
minutos_jogo_titular int;
numero_jogo_titular int;
minutos_entra int;
minutos_sai int;
minutos_total int;
begin
	minutos_entra := (select sum(CAST(tempo_jogo AS INTEGER)) from substituicoes join campeonatos_jogos_equipas
					  on substituicoes.id_jogo = campeonatos_jogos_equipas.id_jogo
					  where substituicoes.id_jogador = jogador and entra = 'true' and campeonatos_jogos_equipas.id_campeonato = campeonato and substituicoes.status = 'true' and campeonatos_jogos_equipas.status = 'true');
	minutos_substituicao_entra := (90 - minutos_entra);
	if minutos_substituicao_entra isnull then
		minutos_substituicao_entra := 0;
		end if;
	
	minutos_substituicao_sai := (select sum(CAST(tempo_jogo AS INTEGER)) from substituicoes 
				where id_jogo in (select id_jogo from campeonatos_jogos_equipas where id_campeonato = campeonato and campeonatos_jogos_equipas.status = 'true') and id_jogador = jogador  and sai = 'true' and substituicoes.status = 'true');
	if minutos_substituicao_sai isnull then
		minutos_substituicao_sai := 0;
		end if;
	
	numero_jogo_titular:= (select count(*) from jogadores_jogos_equipas 
						 
	where id_jogo in(select id_jogo from campeonatos_jogos_equipas where id_campeonato = campeonato and campeonatos_jogos_equipas.status = 'true') and jogadores_jogos_equipas.id_jogo not in (select id_jogo from substituicoes where id_jogador = jogador and substituicoes.status = 'true')  and titular = 'true' and id_jogador = jogador and jogadores_jogos_equipas.status = 'true'
						 );
	if numero_jogo_titular isnull then
		numero_jogo_titular := 0;
	else  	
	minutos_jogo_titular := (90 * numero_jogo_titular);
	end if;
	
	minutos_total := minutos_substituicao_entra + minutos_substituicao_sai + minutos_jogo_titular;
	raise info 'minutos_substituicao_entra % % minutos_substituicao_sai % % minutos_jogo_titular % %  minutos_total %', minutos_substituicao_entra, E'\n',minutos_substituicao_sai, E'\n',minutos_jogo_titular, E'\n',minutos_total;
	return minutos_total;
	end;
$$

