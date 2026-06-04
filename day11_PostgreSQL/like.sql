#start with the following SQL query to find all cars whose model starts with 'M':
SELECT * FROM cars
WHERE model LIKE 'M%';
#To find all cars whose model ends with 'a', use the following query:
SELECT * FROM cars
WHERE model LIKE '%a';
#To find all cars whose model contains 'o', use the following query:
SELECT * FROM cars
WHERE model LIKE '%o%';
#_ underscore with a single character
SELECT * FROM cars
WHERE model LIKE '_a';
#underscore with two characters
SELECT * FROM cars
WHERE model LIKE '__a';
#underscore with three characters
SELECT * FROM cars
WHERE model LIKE '___a';
#To find all cars whose model starts with 'M' and ends with 'a', use the following query:
SELECT * FROM cars
WHERE model LIKE 'M%a';
#To find all cars whose model starts with 'M' and has 'o' as the second character, use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo%';
#To find all cars whose model starts with 'M' and has 'o' as the second character and ends with 'a', use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo%a';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character, use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_a%';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and ends with 's', use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_a%s';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character, use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as%';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and ends with 'a', use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as%a';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and has 'a' as the sixth character, use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as_a%';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and has 'a' as the sixth character and ends with 's', use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as_as';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and has 'a' as the sixth character and has 's' as the seventh character, use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as_as%';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and has 'a' as the sixth character and has 's' as the seventh character and ends with 'a', use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as_as%a';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and has 'a' as the sixth character and has 's' as the seventh character and has 'a' as the eighth character, use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as_as_a%';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and has 'a' as the sixth character and has 's' as the seventh character and has 'a' as the eighth character and ends with 's', use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as_as_as';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and has 'a' as the sixth character and has 's' as the seventh character and has 'a' as the eighth character and has 's' as the ninth character, use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as_as_as%';
#To find all cars whose model starts with 'M' and has 'o' as the second character and has 'a' as the fourth character and has 's' as the fifth character and has 'a' as the sixth character and has 's' as the seventh character and has 'a' as the eighth character and has 's' as the ninth character and ends with 'a', use the following query:
SELECT * FROM cars
WHERE model LIKE 'Mo_as_as_as%a';
#To find all customers whose city starts with 'L', has 'n' as the second character, has 'd' as the fourth character, and has any characters in between, use the following query:
SELECT * FROM customers
WHERE city LIKE 'L_nd__';


