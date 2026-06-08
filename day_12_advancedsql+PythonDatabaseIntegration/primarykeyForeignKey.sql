create table employees (
    employee_id int primary key,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100)
);
-- primary key on alter table
alter table employees
add constraint pk_employee_id primary key (employee_id);
-- composite primary key
create table orders (
    order_id int,
    product_id int,
    quantity int,
    primary key (order_id, product_id)
);
-- primary key with auto-increment
create table customers (
    customer_id int primary key auto_increment,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100)
);
-- primary key with unique constraint
create table products (
    product_id int primary key,
    product_name varchar(100) unique,
    price decimal(10, 2)
);
-- primary key with foreign key
create table order_details (
    order_id int,
    product_id int,
    quantity int,
    primary key (order_id, product_id),
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id)
);
-- drop primary key
alter table employees
drop primary key;
-- add primary key
alter table employees
add primary key (employee_id);
-- modify primary key
alter table employees
drop primary key,
add primary key (employee_id, email);
-- drop foreign key
alter table order_details
drop foreign key fk_order_id;
-- add foreign key
alter table order_details
add constraint fk_order_id foreign key (order_id) references orders(order_id);
-- modify foreign key
alter table order_details
drop foreign key fk_product_id,
add constraint fk_product_id foreign key (product_id) references products(product_id);

