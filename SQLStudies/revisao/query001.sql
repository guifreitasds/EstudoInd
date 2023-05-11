create database revisao01;

use revisao01;

create table Clientes(
	id int primary key auto_increment,
    name varchar(255),
    surname varchar(255),
    mail varchar(255),
    phone varchar(11)
);

insert into clientes (name, surname, mail, phone)
values ("João", "Silva", "joao.silva@gmail.com", "11987654321");


insert into clientes (name, surname, mail, phone)
values ("Marcos", "Aurélio", "marcos@gmail.com", "11999954321");



insert into clientes (name, surname, mail, phone)
values ("Pedro", "Costa", "pedrocosta@yahoo.com.br", "81898981122");

select * from clientes;

create table produtos(
	id int primary key auto_increment,
    name varchar(255),
    description varchar(400),
    price double,
    qtd_in_stock int
);

insert into produtos (name, description, price, qtd_in_stock) 
values ("Camiseta", "Camiseta preta de algodão", 29.90, 100), ("Calça Jeans", "Calça jeans masculina", 89.90, 50), ("Tênis", "Tênis esportivo preto", 129.90, 20);

select * from produtos where qtd_in_stock < 51;

create table alunos(
	id int primary key auto_increment,
    name varchar(255),
    surname varchar(255),
    age int,
    final_grade double
    
);

create table livros (
	id int primary key auto_increment,
    title varchar(255),
    author varchar(255),
	company varchar(255),
    year_of_publication int
);

insert into alunos(name, surname, age, final_grade)
values ("João", "Pedro", 17, 9.0), ("Carlos", "Silva", 18, 7.5), ("Paulo", "Roberto", 16, 8.5), ("Lucas", "Moura", 19, 10);

select name, surname from alunos where age >=18;

insert into livros (title, author, company, year_of_publication)
values ("A Menina que Roubava Livros", "Markus Zusak", "Intrinseca", 2006), ("O Sol é para Todos", "Harper Lee", "José Olympio", 1960), ("O Nome da Rosa", "Umberto Eco", "Record", 1980), ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Agir", 1943);



select title from livros where company = "Intrinseca";



