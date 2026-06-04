#left join 
#To perform a left join between the orders and customers tables based on the customer_id column, use the following query:
SELECT *
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.customer_id;

#left outer join will give same result as left join
SELECT *
FROM orders
LEFT OUTER JOIN customers ON orders.customer_id = customers.customer_id;

