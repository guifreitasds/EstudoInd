select * from gafanhotos where sexo = 'F';

select * from gafanhotos where nascimento between '2000-01-01' and '2015-12-31';

select * from gafanhotos where profissao = 'Programador' and sexo = 'M';

select * from gafanhotos where nacionalidade = 'Brasil' and nome like 'J%' and sexo = 'F';

select nome, nacionalidade from gafanhotos where sexo = 'M' and nome like '%Silva%' and nacionalidade <> 'Brasil' and peso < 100;

select max(altura) from gafanhotos where sexo = 'M' and nacionalidade = 'Brasil'; 
