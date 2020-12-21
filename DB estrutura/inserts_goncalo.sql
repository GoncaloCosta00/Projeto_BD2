insert into modalidades (modalidade) values 
('Futebol'),
('Futsal'),
('Basquete'),
('Voleibol'),
('Hoquei em patins'),
('Andebol');


insert into epocas (ano_inicio,ano_fim) values
(2018,2019),
(2019,2020),
(2020,2021);

insert into campeonatos (id_modalidade,id_epoca,nome_campeonato) values 
--futebol
(1,1,'Primeira Liga'),
(1,2,'Primeira Liga'),
(1,3,'Primeira Liga'),

(1,1,'Segunda Liga'),
(1,2,'Segunda Liga'),
(1,3,'Segunda Liga'),

(1,1,'Campeonato de portugal'),
(1,2,'Campeonato de portugal'),
(1,3,'Campeonato de portugal'),
--futsal
(2,1,'Liga Placard'),
(2,2,'Liga Placard'),
(2,3,'Liga Placard'),
--basquete
(3,1,'Liga portuguesa de Basquete'),
(3,2,'Liga portuguesa de Basquete'),
(3,3,'Liga portuguesa de Basquete'),

(3,1,'Segunda divisão de Basquete'),
(3,2,'Segunda divisão de Basquete'),
(3,3,'Segunda divisão de Basquete'),
--voleibol
(4,1,'Campeonato nacional de voleibol'),
(4,2,'Campeonato nacional de voleibol'),
(4,3,'Campeonato nacional de voleibol'),

(4,1,'Segunda divisão de voleibol'),
(4,2,'Segunda divisão de voleibol'),
(4,3,'Segunda divisão de voleibol'),

(4,1,'Terceira divisão de voleibol'),
(4,2,'Terceira divisão de voleibol'),
(4,3,'Terceira divisão de voleibol'),
--hoquei em patins
(5,1,'Campeonato nacional de hoquei em patins'),
(5,2,'Campeonato nacional de hoquei em patins'),
(5,3,'Campeonato nacional de hoquei em patins'),
--andebol
(6,1,'Andebol 1'),
(6,2,'Andebol 1'),
(6,3,'Andebol 1'),

(6,1,'Andebol 2'),
(6,2,'Andebol 2'),
(6,3,'Andebol 2');


insert into jogos (data_hora, local) values 
('2019-12-22 17:30:00', 'Madeira'),
('2021-04-28 10:25:00', 'Évora'),
('2020-12-09 12:30:00', 'Évora'),
('2020-11-06 15:45:00', 'Madeira'),
('2021-02-26 20:30:00', 'Santarém'),
('2019-08-04 19:40:00', 'Viseu'),
('2021-07-12 20:15:00', 'Évora'),
('2021-07-11 21:15:00', 'Tondela'),
('2019-09-29 21:00:00', 'Viseu'),
('2019-11-23 21:00:00', 'Madeira'),
('2020-04-05 10:00:00', 'Évora'),
('2021-07-08 10:00:00', 'Santarém'),
('2019-11-10 10:00:00', 'Madeira'),
('2021-03-17 10:00:00', 'Tondela'),
('2020-12-20 10:00:00', 'Santarém'),
('2019-03-22 10:00:00', 'Madeira'),
('2019-04-03 10:00:00', 'Évora'),
('2019-07-25 14:00:00', 'Tondela'),
('2021-07-08 14:00:00', 'Santarém'),
('2021-05-07 14:15:00', 'Viseu'),
('2021-08-14 14:15:00', 'Tondela'),
('2020-07-22 14:15:00', 'Viseu'),
('2021-09-23 14:15:00', 'Coimbra'),
('2019-05-17 14:15:00', 'Aveiro'),
('2019-03-25 16:15:00', 'Viseu'),
('2021-04-06 16:25:00', 'Lisboa'),
('2021-05-03 16:25:00', 'Tondela'),
('2021-07-22 16:25:00', 'Faro'),
('2020-08-17 16:25:00', 'Viseu'),
('2021-06-16 16:25:00', 'Porto'),
('2019-09-10 16:25:00', 'Viseu'),
('2020-10-24 16:45:00', 'Coimbra'),
('2019-10-10 18:45:00', 'Faro'),
('2019-01-03 18:45:00', 'Porto'),
('2019-09-29 18:45:00', 'Guarda'),
('2019-01-02 18:45:00', 'Lisboa'),
('2020-06-11 18:45:00', 'Porto'),
('2020-08-30 18:45:00', 'Madeira'),
('2019-08-21 18:45:00', 'Aveiro'),
('2020-08-31 19:30:00', 'Coimbra'),
('2021-04-24 19:30:00', 'Faro'),
('2019-04-08 19:30:00', 'Beja'),
('2020-12-28 19:30:00', 'Viseu'),
('2021-07-23 19:30:00', 'Aveiro'),
('2020-07-02 19:30:00', 'Guarda'),
('2021-07-08 20:22:00', 'Porto'),
('2020-12-28 20:10:00', 'Lisboa'),
('2020-11-23 20:10:00', 'Beja'),
('2021-05-19 20:10:00', 'Lisboa'),
('2019-04-23 20:10:00', 'Guarda'),
('2020-12-28 19:30:00', 'Viseu'),
('2021-07-23 19:30:00', 'Aveiro'),
('2020-07-02 19:30:00', 'Bragança'),
('2021-07-08 20:22:00', 'Vila Real'),
('2020-12-28 20:10:00', 'Lisboa'),
('2020-11-23 20:10:00', 'Beja'),
('2021-05-19 20:10:00', 'Lisboa'),
('2019-04-23 20:10:00', 'Bragança'),
('2020-12-28 19:30:00', 'Braga'),
('2021-07-23 19:30:00', 'Aveiro'),
('2020-07-02 19:30:00', 'Madeira'),
('2021-07-08 20:22:00', 'Braga'),
('2020-12-28 20:10:00', 'Vila Real'),
('2020-11-23 20:10:00', 'Beja'),
('2021-05-19 20:10:00', 'Braga'),
('2019-04-23 20:10:00', 'Bragança'),
('2020-12-28 19:30:00', 'Braga'),
('2021-07-23 19:30:00', 'Vila Real'),
('2020-07-02 19:30:00', 'Madeira'),
('2021-07-08 20:22:00', 'Porto'),
('2020-12-28 20:10:00', 'Lisboa'),
('2020-11-23 20:10:00', 'Beja'),
('2021-05-19 20:10:00', 'Bragança'),
('2019-04-23 20:10:00', 'Madeira'),
('2019-05-18 20:10:00', 'Viseu');
