SELECT product_name
FROM products
WHERE product_id = ANY (
  SELECT product_id
  FROM order_details
  WHERE quantity > 120
);