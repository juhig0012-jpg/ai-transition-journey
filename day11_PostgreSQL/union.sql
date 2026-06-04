SELECT product_id, product_name
FROM products
UNION
SELECT testproduct_id, product_name
FROM testproducts
ORDER BY product_id;

SELECT product_id
FROM products
UNION ALL
SELECT testproduct_id
FROM testproducts
ORDER BY product_id;