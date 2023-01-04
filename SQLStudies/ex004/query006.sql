select profissao, count(*) as qtd_pessoas from gafanhotos
group by profissao
order by qtd_pessoas desc;