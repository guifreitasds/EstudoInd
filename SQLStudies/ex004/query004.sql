select * from gafanhotos where sexo = 'F';

select * from gafanhotos where nascimento between '2000-01-01' and '2015-12-31';

select * from gafanhotos where profissao = 'Programador' and sexo = 'M';

select * from gafanhotos where nacionalidade = 'Brasil' and nome like 'J%' and sexo = 'F';

select nome, nacionalidade from gafanhotos where sexo = 'M' and nome like '%Silva%' and nacionalidade <> 'Brasil' and peso < 100;

select max(altura) from gafanhotos where sexo = 'M' and nacionalidade = 'Brasil';

select avg(peso) from gafanhotos;

select min(peso) from gafanhotos where nacionalidade <> 'Brasil' and nascimento between '1990-01-01' and '2000-12-31' and sexo = 'F';

select * from gafanhotos where peso = '35.90' 
