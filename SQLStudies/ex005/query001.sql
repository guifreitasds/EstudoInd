alter table gafanhotos
add column cursopreferido int;

alter table gafanhotos
add foreign key(cursopreferido) 
references cursos(idcurso);

select * from gafanhotos;
select * from cursos;

delete from cursos 
where idcurso='6';

update gafanhotos
set cursopreferido = '6'
where id = '1';
