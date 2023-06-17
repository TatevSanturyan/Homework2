create database library

create table authors
(
    id         smallserial primary key,
    first_name varchar(10),
    last_name  varchar(20)
);
create table books
(
    id                   smallserial primary key,
    title                varchar(100) not null,
    year_first_published smallserial
);
create table BookAuthors
(
    author_id integer references authors (id),
    book_id   integer references books (id)
);
create table students
(
    id         smallserial primary key,
    first_name varchar(20)  not null,
    last_name  varchar(30)  not null,
    email      varchar(255) not null


);
create table book_copies
(
    id             smallserial primary key,
    book_id        integer references books (id),
    isbn           varchar(13) unique not null,
    year_published smallserial
);
create table borrows
(
    id            smallserial primary key,
    book_copy_id  integer references book_copies (id),
    student_id    integer references students (id),
    borrowed_date date not null default now(),
    return_date   date
);