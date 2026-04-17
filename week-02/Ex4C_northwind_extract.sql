-- 4a) What is the name of the table that holds the items Northwind sells?
-- The name of the table that holds the items Nortwind sell is products. We can see the product names with the query below.
SELECT *
FROM products

-- 4b) What is the name of the table that holds the types/categories of the items Northwind sells
-- Categories table holds the item categories and can be seen with the query below.
SELECT *
FROM categories

-- 5 Create a SELECT statement to retrieve all columns from the employees table
-- 5A)  Who is the Northwind employee whose name makes it look like she’s a bird?
-- Include the answer as a comment underneath the SELECT statement.
SELECT *
FROM employees 
LIMIT 1

SELECT DISTINCT FirstName, LastName
FROM employees 
-- Margaret Peacock

-- 6) Create a SELECT statement to retrieve all columns from the products table.

SELECT * 
FROM products

-- a) How many records does your query return? Using the toolbar options at the top of 
-- the query pane, how can you change your query to retrieve only 10 rows? Include 
-- the answer as a comment underneath the SELECT statement.

-- ANSWER: We retrieved 77 results with the query above on line 24 and 25.
-- We can change the Limit to 10 rows with the option on the panel 
-- or we can add LIMIT 10 at the and of the query as below 
SELECT * 
FROM products
LIMIT 10

-- b) BONUS: How could you write the query to limit the number of rows returned? This 
-- isn’t covered in the Week 2 Student Guide, so if you tackle this bonus question, 
-- you’ll need to do a little independent research. Add the answer as a comment in 
-- your script with a note on what source you used to find the answer

-- ANSWER: We can use LIMIT 10, LIMIT 50 etc. at the end of the query
-- Or if we are using SQL Server we can use SELECT TOP 10 * FROM products
-- Or of we are using Oracle we would use FETCH FIRST 10 ROWS ONLY;


-- 7) Create another SELECT statement to retrieve all columns from the categories table
-- a) The category ID for Seafood is 8
SELECT * 
FROM categories

-- 8a) Create a final SELECT statement to retrieve the top 50 records from orders, including 
-- only the OrderID, OrderDate, ShipName, and ShipCountry columns.

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50