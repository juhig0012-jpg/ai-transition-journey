SELECT COUNT(customer_id), country
FROM customers
GROUP BY country;

SELECT customers.customer_name, COUNT(orders.order_id)
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customer_name;