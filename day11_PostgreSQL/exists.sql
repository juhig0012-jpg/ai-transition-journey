SELECT customers.customer_name
FROM customers
WHERE EXISTS (
  SELECT order_id
  FROM orders
  WHERE customer_id = customers.customer_id
);

SELECT customers.customer_name
FROM customers
WHERE NOT EXISTS (
  SELECT order_id
  FROM orders
  WHERE customer_id = customers.customer_id
);