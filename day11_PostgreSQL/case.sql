SELECT product_name,
CASE
  WHEN price < 10 THEN 'Low price product'
  WHEN price > 50 THEN 'High price product'
ELSE
  'Normal product'
END
FROM products;

SELECT product_name,
CASE
  WHEN price < 10 THEN 'Low price product'
  WHEN price > 50 THEN 'High price product'
ELSE
  'Normal product'
END AS "price category"
FROM products;