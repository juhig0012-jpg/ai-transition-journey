#full join
#To perform a full join between the orders and customers tables based on the customer_id column, use the following query:
SELECT *
FROM orders
FULL JOIN customers ON orders.customer_id = customers.customer_id;
#full outer join will give same result as full join
SELECT *
FROM orders
FULL OUTER JOIN customers ON orders.customer_id = customers.customer_id;