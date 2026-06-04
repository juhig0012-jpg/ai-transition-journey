#cross join is used to combine each row from the first table with each row from the second table, resulting in a Cartesian product of the two tables.
#To perform a cross join between the orders and customers tables, use the following query:
SELECT *
FROM orders
CROSS JOIN customers;
#cross join can also be written using the comma operator
SELECT *
FROM orders, customers;