select * from gafanhotos
where nome like '%Silva%';

select distinct nacionalidade from gafanhotos;


select count(*) from cursos;

select count(*) from cursos 
where carga > 40;

select max(totaulas) from cursos;

select min(carga) from cursos;