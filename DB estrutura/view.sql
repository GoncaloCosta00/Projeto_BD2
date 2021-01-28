drop view if exists view2;
drop function if exists view2_func;
create or replace function view2_func()
returns table (
	 "_id_jogo" integer,
	 "_data_do_jogo" date,
	 "_id_campeonato" integer,
	 "_Equipa A" integer,
	 "_A vs B" text,
	 "_Equipa B" integer,
	 "_Goleador da equipa A" text,
	 "_Goleador da equipa B" text,
	  "_Jogador + _penalizado_equipa A" text,
	  "_Jogador + _penalizado_equipa B" text
	)
as
$$
	declare
	
	begin
		return query (select 
	jogos.id_jogo,jogos.data_hora as "data do jogo",
	(select 
		id_campeonato 
		from campeonatos_jogos_equipas 
		where 
			campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
		limit 1
		),
		(select 
		id_equipa 
		from campeonatos_jogos_equipas 
		where 
			campeonatos_jogos_equipas.id_campeonato = (select 
				id_campeonato 
				from campeonatos_jogos_equipas 
				where 
					campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
				limit 1
				) and
			campeonatos_jogos_equipas.id_jogo = jogos.id_jogo 
		order by id_equipa asc 
		limit 1
		) as "Equipa A",
    (calcular_golos_equipa_num_jogo((select 
		id_equipa 
		from campeonatos_jogos_equipas 
		where 
			campeonatos_jogos_equipas.id_campeonato = (select 
				id_campeonato 
				from campeonatos_jogos_equipas 
				where 
					campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
				limit 1
				) and
			campeonatos_jogos_equipas.id_jogo = jogos.id_jogo 
		order by id_equipa asc 
		limit 1
		),
		jogos.id_jogo
	)) || ' vs ' ||
	(calcular_golos_equipa_num_jogo((select 
		id_equipa 
		from campeonatos_jogos_equipas 
		where 
			campeonatos_jogos_equipas.id_campeonato = (select 
				id_campeonato 
				from campeonatos_jogos_equipas 
				where 
					campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
				limit 1
				) and
			campeonatos_jogos_equipas.id_jogo = jogos.id_jogo 
		order by id_equipa desc 
		limit 1
		),
		jogos.id_jogo
	)) as "A vs B",  
	(select 
		id_equipa 
		from campeonatos_jogos_equipas 
		where 
			campeonatos_jogos_equipas.id_campeonato = (select 
				id_campeonato 
				from campeonatos_jogos_equipas 
				where 
					campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
				limit 1
				) and
			campeonatos_jogos_equipas.id_jogo = jogos.id_jogo 
		order by id_equipa desc 
		limit 1
		) as "Equipa B",
		(SELECT 
			jogadores.nome 
			from jogadores inner 
			join jogam
				on jogadores.id_jogador = jogam.id_jogador
                inner join equipas
					on jogam.id_equipa = equipas.id_equipa 
					inner join pontuacoes_jogadores_jogos
						on pontuacoes_jogadores_jogos.id_jogador = jogadores.id_jogador
            where
				pontuacoes_jogadores_jogos.id_jogo =jogos.id_jogo and 
				equipas.id_equipa = (select 
					id_equipa 
					from campeonatos_jogos_equipas 
					where 
						campeonatos_jogos_equipas.id_campeonato = (select 
							id_campeonato 
							from campeonatos_jogos_equipas 
							where 
								campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
							limit 1
							) and
						campeonatos_jogos_equipas.id_jogo = jogos.id_jogo 
					order by id_equipa 
					limit 1
					)
            group by jogadores.nome
			ORDER BY COUNT(pontuacoes_jogadores_jogos.id_jogador) desc
			limit 1
		) as "Goleador da equipa A",
		(SELECT 
			jogadores.nome 
			from jogadores inner 
			join jogam
				on jogadores.id_jogador = jogam.id_jogador
                inner join equipas
					on jogam.id_equipa = equipas.id_equipa 
					inner join pontuacoes_jogadores_jogos
						on pontuacoes_jogadores_jogos.id_jogador = jogadores.id_jogador
            where
				pontuacoes_jogadores_jogos.id_jogo =jogos.id_jogo and 
				equipas.id_equipa = (select 
					id_equipa 
					from campeonatos_jogos_equipas 
					where 
						campeonatos_jogos_equipas.id_campeonato = (select 
							id_campeonato 
							from campeonatos_jogos_equipas 
							where 
								campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
							limit 1
							) and
						campeonatos_jogos_equipas.id_jogo = jogos.id_jogo 
					order by id_equipa desc 
					limit 1
					)
            group by jogadores.nome
			ORDER BY COUNT(pontuacoes_jogadores_jogos.id_jogador) desc
			limit 1
		) as "Goleador da equipa B",
   			(SELECT jogadores.nome from jogadores inner join jogam on jogadores.id_jogador = jogam.id_jogador
                inner join equipas on jogam.id_equipa = equipas.id_equipa 
                
                inner join jogos_jogadores_acoesdiscip on jogos_jogadores_acoesdiscip.id_jogador = jogadores.id_jogador
                
               where  jogos_jogadores_acoesdiscip.id_jogo =jogos.id_jogo and 
				equipas.id_equipa = (select id_equipa from campeonatos_jogos_equipas 
					where campeonatos_jogos_equipas.id_campeonato = (select id_campeonato 
							from campeonatos_jogos_equipas 
							where campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
							limit 1 ) and campeonatos_jogos_equipas.id_jogo = jogos.id_jogo 
					order by id_equipa 
					limit 1
					)
                
                group by jogadores.nome ORDER BY COUNT(jogos_jogadores_acoesdiscip.id_jogador) desc limit 1)  as "Jogador + penalizado equipa A",
   (SELECT jogadores.nome from jogadores inner join jogam on jogadores.id_jogador = jogam.id_jogador
                inner join equipas on jogam.id_equipa = equipas.id_equipa 
                
                inner join jogos_jogadores_acoesdiscip on jogos_jogadores_acoesdiscip.id_jogador = jogadores.id_jogador
                
               where  jogos_jogadores_acoesdiscip.id_jogo =jogos.id_jogo and 
				equipas.id_equipa = (select id_equipa from campeonatos_jogos_equipas 
					where campeonatos_jogos_equipas.id_campeonato = (select id_campeonato 
							from campeonatos_jogos_equipas 
							where campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
							limit 1 ) and campeonatos_jogos_equipas.id_jogo = jogos.id_jogo 
					order by id_equipa desc
					limit 1
					)
                
                group by jogadores.nome ORDER BY COUNT(jogos_jogadores_acoesdiscip.id_jogador) desc limit 1)  as "Jogador + penalizado equipa B"
   
   
        from jogos
   where (select 
		id_campeonato 
		from campeonatos_jogos_equipas 
		where 
			campeonatos_jogos_equipas.id_jogo = jogos.id_jogo
		limit 1) is not null
					 order by jogos.data_hora );
	end;
$$
language plpgsql;

drop view if exists view2;
create view view2
as select * from view2_func();