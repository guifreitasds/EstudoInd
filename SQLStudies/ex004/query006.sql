select profissao, count(*) as qtd_pessoas from gafanhotos
group by profissao
order by qtd_pessoas desc;

select sexo, count(*) as qtd_pessoas from gafanhotos
where nascimento > '2005-01-01'
group by sexo;

select nacionalidade, count(*) as qtd_pessoas from gafanhotos
where nacionalidade != 'Brasil'
group by nacionalidade 
having qtd_pessoas > 3;