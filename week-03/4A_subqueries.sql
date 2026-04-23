USE northwind;

-- 1. What is the product name(s) of the most expensive products?

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products)

-- Cte de Blaye	263.5000

-- 2. What is the product name(s) and categories of the least expensive products?

SELECT p.ProductName, c.CategoryName
FROM products AS p
JOIN categories AS c ON c.CategoryID = p.CategoryID
WHERE p.UnitPrice = (SELECT MIN(UnitPrice) FROM products)

-- Geitost	Dairy Products

-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?

SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName
FROM orders AS o
JOIN shippers AS s ON s.ShipperID = o.ShipVia
WHERE o.ShipVia = (SELECT ShipperID FROM shippers WHERE CompanyName = 'Federal Shipping')

-- I didn't have to use JOIN function here. But I wanted to see CompanyName column on my result so I joined tables and s.CompanyName
-- column here.

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?

SELECT od.OrderID , p.ProductName
FROM `order details` AS od
JOIN products AS p ON od.ProductID = p.ProductID
WHERE p.ProductID = (SELECT ProductID FROM products WHERE ProductName LIKE '%Sasquatch Ale%')

-- There are 19 orderIDs that included Sasquatch Ale

-- 5. What is the name of the employee that sold order 10266?

SELECT FirstName, LastName
FROM employees
WHERE EmployeeID = (SELECT EmployeeID FROM orders WHERE orderID = 10266)

-- Janet	Leverling

-- 6. What is the name of the customer that bought order 10266?

SELECT CompanyName, ContactName
FROM customers
WHERE CustomerID = (SELECT CustomerID FROM orders WHERE OrderID = 10266)

-- Wartian Herkku	Pirkko Koskitalo

