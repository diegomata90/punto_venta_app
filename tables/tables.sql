--- Creacion de tabla Producto , categoria y marca

create table IF NOT EXISTS category (
    id_category SERIAL primary key not null,
    code VARCHAR (50) UNIQUE not null,
    name VARCHAR (100) not null
);


create table IF NOT EXISTS brand(
    id_brand SERIAL primary key not null,
    code varchar(50) UNIQUE not null,
    name varchar (100) not null
);


create table IF NOT EXISTS product (
    id_product SERIAL primary key not NULL,
    code VARCHAR(50) UNIQUE not NULL, 
    name VARCHAR(100) not NULL,
    cost NUMERIC(10,2) not NULL,
    price NUMERIC(10,2)  not NULL,
    stock NUMERIC(10,2)  not NULL,
    state VARCHAR(50) not NULL,
    created_at TIMESTAMP not NULL DEFAULT CURRENT_TIMESTAMP,
    image VARCHAR(100),
    id_category INTEGER not NULL,
    id_brand INTEGER not null,
    CONSTRAINT fk_product_category FOREIGN KEY (id_category) REFERENCES category(id_category),
    constraint fk_product_brand foreign key (id_brand) references brand(id_brand)
);

--- Creacion de tabla usuarios y rol


CREATE TABLE IF NOT EXISTS role (
    id_role SERIAL PRIMARY KEY NOT NULL,
    code VARCHAR(50) unique NOT NULL,
    name VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS users (
    id_user SERIAL PRIMARY key not NULL,
    code VARCHAR(50) unique NOT NULL,
    username VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    avatar VARCHAR(100),
    id_role INTEGER not NULL,
    created_at TIMESTAMP not NULL DEFAULT CURRENT_TIMESTAMP,
    constraint fk_users_role foreign key (id_role) references role(id_role)
);

-- Create the customers table
CREATE TABLE IF NOT EXISTS customer (
    id_customer SERIAL PRIMARY KEY NOT NULL,
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    email VARCHAR(100),
    phone VARCHAR(20)
);


-- Creación de la tabla de facturación encabezado
CREATE TABLE IF NOT EXISTS invoice_header(
    id_iheader SERIAL PRIMARY KEY NOT NULL,
    invoice_number VARCHAR(20) NOT NULL UNIQUE,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(10,2) NOT NULL,
    id_customer INTEGER NOT NULL,
	id_user INTEGER not null,    
    CONSTRAINT fk_invoice_header_customer foreign key (id_customer) references customer(id_customer),
    CONSTRAINT fk_invoice_header_user foreign key (id_user) references users(id_user)
);

CREATE TABLE IF NOT EXISTS invoice_detail(
    id_idetail SERIAL PRIMARY KEY NOT NULL,
    quantity INTEGER NOT NULL,
    cost NUMERIC(10,2) NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,
    subtotal NUMERIC(10, 2) NOT NULL,
    id_iheader INTEGER NOT NULL,
    id_product INTEGER NOT NULL,
    CONSTRAINT fk_invoice_detail_iheader FOREIGN KEY (id_iheader) REFERENCES invoice_header(id_iheader),
    CONSTRAINT fk_invoice_detail_product FOREIGN KEY (id_product) REFERENCES product(id_product)
);

/* Eliminar Tablas

drop table invoice_detail ;
drop table invoice_header ;
drop table users;
drop table role;
drop table customer;
drop table product;
drop table brand;
drop table category ;

*/