#right join
#To perform a right join between the orders and customers tables based on the customer_id column, use the following query:
SELECT *
FROM orders
RIGHT JOIN customers ON orders.customer_id = customers.customer_id;
#right outer join will give same result as right join
SELECT *
FROM orders
RIGHT OUTER JOIN customers ON orders.customer_id = customers.customer_id;