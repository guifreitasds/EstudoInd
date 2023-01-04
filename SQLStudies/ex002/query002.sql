insert into cursos 
(nome, descricao, carga, totaulas, ano)
values
('HTML4', 'CURSO DE HTML5', '40', '37', '2014'),
('Algoritmos', 'Lógica de programação', '20', '15', '2014'),
('Photoshop', 'Dicas de photoshop CC', '10', '8', '2014'),
('PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('Jarva', 'Introdução à linguagem JAVA', '10', '29', '2000'),
('MySQL', 'Banco de dados MySQL', '30', '15', '2016'),
('Word', 'Curso completo de word', '40', '30', '2016'),
('Sapateado', 'Danças ritmicas', '40', '30', '2018'),
('Cozinha árabe', 'Aprenda a fazer kibe', '40', '30', '2018'),
('Youtuber', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

select * from people;

update cursos set nome='HTML5' where idcurso ='1';

update cursos set nome='PHP', ano='2015' where idcurso='4';

update cursos set nome='Java', ano='2015', carga='40' where idcurso='5'; 

update cursos set descricao='Curso de HTML5' where nome='HTML5';