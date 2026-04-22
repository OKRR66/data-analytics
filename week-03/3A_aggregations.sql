USE northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. 
-- Then write a second query to find the name of the product that has that price.
SELECT MIN(UnitPrice)
FROM products

SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice ASC
LIMIT 1

-- 2. Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
-- using the ROUND function to round the average price to the nearest cent.)

SELECT Round(AVG(UnitPrice), 2)
FROM products

-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.

SELECT MAX(UnitPrice)
FROM products

SELECT p.ProductName, s.CompanyName, p.UnitPrice
FROM products AS p
JOIN suppliers AS s ON s.SupplierID = p.SupplierID
WHERE 
	p.UnitPrice = ( SELECT MAX(UnitPrice) FROM products)
    
-- I Used the result of first query (263.5000) on my WHERE section on the second query. But it felt odd.
-- I asked Claude how can I use a subquery here and improved my query accordingly.

 -- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).
 
SELECT ROUND(SUM(Salary) , 2) AS total_monthly_salary
FROM employees

-- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes. 
-- Just the amounts, not the specific employees!

SELECT MAX(Salary), MIN(Salary)
FROM employees

-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply.
-- Hint: Join is your friend here.

SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS number_of_products
FROM suppliers AS s
JOIN products AS p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY number_of_products

-- 7. Write a query to find the list of all category names and the average price for items in each category.

SELECT c.CategoryName, c.CategoryID, ROUND(AVG(p.UnitPrice) , 2) AS avg_unit_price
FROM categories AS c
JOIN products AS p ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName, c.CategoryID

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply.

SELECT s.CompanyName, COUNT(p.ProductID) AS Units_Provided
FROM suppliers AS s
JOIN products AS p ON p.SupplierID = s.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5

-- My original query was including WHERE instead of HAVING but I figured out that WHERE cannot work after GROUP BY.
-- WHERE is filtering raw rows but after using GROUP BY we must use HAVING

-- 9. Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID, ProductName, (UnitsInStock * UnitPrice) AS Inv_Value
FROM products
WHERE UnitsInStock > 0
ORDER BY Inv_value DESC, ProductName

-- I wanted to show Inv_Value as dollar amount and round it to two decimals. But I couldn't figure out. I am assuming that
-- using alias in ORDER BY causing this issue, but i am not sure how can I work around it to show it as $

