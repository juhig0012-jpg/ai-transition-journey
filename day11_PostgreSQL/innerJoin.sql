#matching records from two tables based on a related column between them or common in both tables
#To perform an inner join between the orders and customers tables based on the customer_id column, use the following query:
SELECT *
FROM orders 
INNER JOIN customers ON orders.customer_id = customers.customer_id;