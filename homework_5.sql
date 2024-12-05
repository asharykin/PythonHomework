-- homework_5_1
SELECT product_name
FROM products
WHERE unit_price >= 3 AND unit_price < 7;

-- homework_5_2
SELECT MIN(unit_price) AS min_price
FROM products
WHERE category_id = 1;

-- homework_5_3
SELECT supplier_id, MAX(unit_price) AS max_price
FROM products
WHERE supplier_id IN (1, 3, 5)
GROUP BY supplier_id
ORDER BY supplier_id;