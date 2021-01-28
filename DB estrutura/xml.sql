select 
	XMLELEMENT (
		name "Jogadores",
		XMLAGG(
			XMLELEMENT (
				name "Jogador",
				xmlforest(
					id_jogador as "ID",
					nome as "Nome",
					telemovel as "Telemovel",
					altura as "Altura",
					naturalidade as "Naturalidade",
					data_nascimento as "DataNascimento",
					(
						select
							equipas.equipa
						from equipas
						inner join jogam
							on equipas.id_equipa = jogam.id_equipa
						where jogam.id_jogador = jogadores.id_jogador
					) as "Equipa",
					(
						select
							clube.nome 
						from equipas
						inner join clube 
							on equipas.id_clube = clube.id_clube
							inner join jogam
								on equipas.id_equipa = jogam.id_equipa
						where jogam.id_jogador = jogadores.id_jogador
					) as "Clube",
					(
						select
							count(id_jogador)
						from pontuacoes_jogadores_jogos
						where
							pontuacoes_jogadores_jogos.id_jogador = jogadores.id_jogador and
							id_jogo in (
								select 
									id_jogo
								from campeonatos_jogos_equipas 
								where 
									id_campeonato = (
										select max(id_campeonato) from campeonatos_jogos_equipas
									)
							)
					) as "Golos",
					(
						select
							count(id_jogador)
						from jogos_jogadores_acoesdiscip
						where
							jogos_jogadores_acoesdiscip.id_jogador = jogadores.id_jogador and
							id_jogo in (
								select 
									id_jogo
								from campeonatos_jogos_equipas 
								where 
									id_campeonato = (
										select max(id_campeonato) from campeonatos_jogos_equipas
									)
							)
					) as "Ações_Disciplinares"
				)
			)
		)
	)
from jogadores;	