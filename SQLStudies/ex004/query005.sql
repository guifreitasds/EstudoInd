select carga, count(nome) as qtd_cursos from cursos group by carga;

select totaulas, count(*) from cursos group by totaulas;

select ano, count(*) as qtd_cursos from cursos 
group by ano having qtd_cursos>=4 order by count(*) desc;

select avg(carga) from cursos;

select carga, count(*) as qtd_cursos from cursos
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos);