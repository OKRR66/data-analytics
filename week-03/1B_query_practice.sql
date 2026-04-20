USE northwind

-- Ex1B Questions
-- 1. Write a query to list the product id, product name, and unit price of every product that
-- Northwind sells. (Hint: To help set up your query, look at the schema preview to see
-- what column names belong to each table. Or use SELECT * to query all columns
-- first, then refine your query to just the columns you want.)

SELECT ProductID, ProductName, UnitPrice
FROM products

-- 2. Write a query to identify the products where the unit price is $7.50 or less.

SELECT *
FROM products
WHERE unitprice <= 7.50

-- 3. What are the products that we carry where we have no units on hand, 
-- but 1 or more units are on backorder? Write a query that answers this question.

SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock = 0
  AND UnitsOnOrder >= 1
  
-- 4.  Examine the products table. How does it identify the type (category) of each item sold? 
-- Where can you find a list of all categories? 
-- Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry.

SELECT *
FROM products

-- The product table identifies the category of an item with CategoryID column. IDs are numerical values like 1,2,3 etc.
-- The CategoryName and CategoryID are given together in the categories table.
-- I wrote the query below to find all the category names.

SELECT CategoryID, CategoryName
FROM categories

-- Seafood categoryID is 8. So I can use the query below to list all the seafood items we carry.

SELECT *
FROM products
WHERE CategoryID = 8 
	AND UnitsInStock > 0
    
-- 5. Examine the products table again. How do you know what supplier each product comes from? 
-- Where can you find info on suppliers?
-- Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.

-- We can use the SupplierID given in the product table to know what supplier the product comes from. 
-- We can use Suppliers Table to see SupplierID - CompanyName matches.

SELECT SupplierID, CompanyName
FROM suppliers

-- The SupplierID for Tokyo Traders is 4.
-- We can write the query below to see all the products from Tokyo Traders

SELECT *
FROM products
WHERE SupplierID = 4

-- How many employees work at northwind? 
-- What employees have "manager" somewhere in their job title? 
-- Write queries to answer each question.

-- The query below will find the numbers of employess

SELECT *
FROM employees
-- There are 9 employees at Nortwind.

-- I can use the query below to find the employees have "manager" somewhere in their job title 

SELECT Title, EmployeeID, FirstName, LastName
FROM employees
WHERE Title LIKE '%Manager%'

