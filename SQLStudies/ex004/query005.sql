select carga, count(nome) as qtd_cursos from cursos group by carga;

select totaulas, count(*) from cursos group by totaulas;

select ano, count(*) as qtd_cursos from cursos 
group by ano having qtd_cursos>=4 order by count(*) desc;