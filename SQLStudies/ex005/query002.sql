select g.nome, c.nome as nomecurso from gafanhotos as g
join cursos as c
on c.idcurso = g.cursopreferido
order by nomecurso;

select g.nome, c.nome as nomecurso from gafanhotos as g
left join cursos as c
on c.idcurso = g.cursopreferido
order by nomecurso;

select g.nome, c.nome as nomecurso from gafanhotos as g
right join cursos as c
on c.idcurso = g.cursopreferido
order by nomecurso;