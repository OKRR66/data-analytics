USE northwind;

-- 1. Create a single query to list the product id, product name, unit price and category 
-- name of all products. Order by category name and within that, by product name

SELECT p.productID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products AS p 
JOIN categories AS c
ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName

-- 2. Create a single query to list the product id, product name, unit price 
-- and supplier name of all products that cost more than $75. Order by product name.

SELECT p.productID, p.ProductName, p.UnitPrice, s.CompanyName
FROM products AS p
JOIN suppliers AS s
ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY p.ProductName

-- 3. Create a single query to list the product id,
-- product name, unit price, category name, and supplier name of every product. Order by product name.

SELECT p.productID, p.ProductName, p.UnitPrice, s.CompanyName, c.CategoryName
FROM products AS p
JOIN suppliers AS s ON p.SupplierID = s.SupplierID
JOIN categories AS c ON p.CategoryID = c.CategoryID
ORDER BY p.ProductName

-- 4. Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
-- shipped to.

SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName AS Shipper
FROM orders AS o
JOIN shippers AS s ON s.ShipperID = o.ShipVia
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper, o.ShipName

-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by
-- ship name, with a count of how many orders were shipped for that ship name.

SELECT o.ShipName,
       COUNT(o.OrderID) AS OrderCount,
       o.ShipAddress,
       s.CompanyName AS Shipper
FROM orders AS o
JOIN shippers AS s ON s.ShipperID = o.ShipVia
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName, o.ShipAddress, s.CompanyName
ORDER BY Shipper, o.ShipName;
-- I wasn't able to run this quesry at first because I only used o.ShipName on GROUP BY line. I couldn't understand why
-- we need ShipAddress and CompanyName in group by. I took help from Claude for this and it says
-- The rule: every column in SELECT must either be inside COUNT( ) / SUM( ) / etc.
-- or appear in GROUP BY. No exceptions.

-- 6. Create a single query to list the order id, order date, ship name, ship address of all
-- orders that included Sasquatch Ale.
SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress, p.ProductName
FROM orders AS o
JOIN `order details` AS od ON od.OrderID = o.OrderID
JOIN products AS p ON p.ProductID = od.ProductID
WHERE p.ProductName LIKE '%Sasquatch Ale%'
