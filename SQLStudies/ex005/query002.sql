select g.nome, c.nome as nomecurso from gafanhotos as g
join cursos as c
on c.idcurso = g.cursopreferido
order by nomecurso;