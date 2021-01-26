--drop function calcular_golos_equipa_num_jogo() if exists;
create or replace function calcular_golos_equipa_num_jogo(equipa int, jogo int)
returns int 
language plpgsql
as $$
begin
	return(select 
    count(*)
from pontuacoes_jogadores_jogos
where id_jogo= jogo and id_jogo in (select id_jogo from jogadores_jogos_equipas where id_equipa = equipa) and id_jogador in (select id_jogador from jogadores_jogos_equipas where id_equipa = equipa));
		   end;
$$

