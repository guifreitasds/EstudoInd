select * from gafanhotos
where nome like '%Silva%';

select distinct nacionalidade from gafanhotos;


select count(*) from cursos;

select count(*) from cursos 
where carga > 40;

select nome, max(totaulas) from cursos;

select nome, min(carga) from cursos;

select sum(totaulas) from cursos where ano = '2016';

select avg(totaulas) from cursos;