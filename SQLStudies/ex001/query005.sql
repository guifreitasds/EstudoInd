alter table pessoas
add column profissao varchar(10);

select * from pessoas;

alter table pessoas
drop column profissao;

alter table pessoas
modify column profissao varchar(20);

alter table pessoas
change column prof profissao varchar(20);

alter table pessoas 
rename to people;