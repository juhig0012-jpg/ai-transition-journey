SELECT customer_id AS id
FROM customers;
#concatenate first_name and last_name into full_name
SELECT first_name || ' ' || last_name AS full_name
FROM customers;
#aliias name with more than 1 word should be enclosed in double quotes
SELECT first_name || ' ' || last_name AS "Full Name"
FROM customers;