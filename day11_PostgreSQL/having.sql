SELECT COUNT(customer_id), country
FROM customers
GROUP BY country
HAVING COUNT(customer_id) > 5;

SELECT order_id, SUM(order_details.quantity * products.price)
FROM order_details
LEFT JOIN products on products.product_id = order_details.product_id
GROUP BY order_id
HAVING SUM(order_details.quantity * products.price) > 400.00;

SELECT customers.customer_name,
SUM(order_details.quantity * products.price)
FROM order_details
INNER JOIN products ON order_details.product_id = products.product_id
INNER JOIN orders ON order_details.order_id = orders.order_id
INNER JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_id, customers.customer_name
HAVING SUM(order_details.quantity * products.price) >= 1000;