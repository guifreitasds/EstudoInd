select idcurso,nome,ano from cursos order by ano,nome;

select nome, descricao, carga from cursos 
where ano <= '2015' 
order by nome;

select nome, descricao, carga, ano from cursos 
where ano between '2014' and '2016' 
order by ano,nome;

select nome, descricao, carga, ano from cursos 
where ano in (2014, 2016) 
order by ano,nome;

select nome, carga, totaulas from cursos
where carga > 35 and totaulas < 30;

select nome, carga, totaulas from cursos
where carga > 35 or totaulas < 30;

