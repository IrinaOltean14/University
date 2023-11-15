USE Lab1

-- insert data
INSERT INTO Supplier(SID, name, phoneNumber) values (4, 'Color Supplier', '0745 312 298')
INSERT INTO Supplier(SID, name, phoneNumber) values (5, 'InnovationSupplies', '0747 567 099')

INSERT INTO Categories(CID, name) values (4, 'markers for white board')
INSERT INTO Categories(CID, name) values (5, 'highlighter markers')

INSERT INTO Products(PID, name, SID, CID, price, quantity) values (4, 'Green marker', 4, 4, 5, 50)
INSERT INTO Products(PID, name, SID, CID, price, quantity) values (5, 'Neon yellow marker', 4, 5, 3, 25)

INSERT INTO Sale(saleID, saleDate, EID) values (4, '2023-10-23', 2)
INSERT INTO Sale(saleID, saleDate, EID) values (5, '2023-10-21', 2)

INSERT INTO SaleProducts(saleID, PID, quantity) values (4, 4, 5)
INSERT INTO SaleProducts(saleID, PID, quantity) values (5, 5, 6)

INSERT INTO Supplier(SID, phoneNumber) values (6, '0745 378 298')

-- insert that violates the referential integrity constraints 
INSERT INTO Sale(saleID, saleDate, EID) values (6, '2023-10-23', 10) -- foreign key constraint, there is no employee with ID 10

-- update data
UPDATE Promotion
SET discountPercentage = 10
WHERE discountPercentage > 15

UPDATE Products
SET quantity = quantity + 50
WHERE CID = 3 
	AND price > 10

UPDATE Employee
SET salary = 3000
WHERE salary BETWEEN 2300 AND 2700

-- delete data
DELETE FROM Supplier
WHERE name IS NULL

DELETE FROM Products
WHERE name LIKE '%Blue%'

-- UNION with OR: select all the products that are made by the supplier with 'Office Supplies' or 'XYZ Supplier'
SELECT P.name, P.price
FROM Products P, Supplier S
WHERE P.SID = S.SID AND (S.name = 'Office Supplies' OR S.name = 'XYZ Supplier')
ORDER BY P.price

-- UNION with UNION: get all orders placed by Maria or from the supplier with the name 'XYZ Supplier'
SELECT O.OID, O.orderDate
FROM Orders O, Supplier S
WHERE S.SID = O.SID AND S.name = 'XYZ Supplier'
UNION
SELECT O.OID, O.orderDate
FROM Orders O, Employee E
WHERE O.EID = E.EID AND E.firstName = 'Maria'
ORDER BY O.orderDate

--INTERSECTION with INTERSECT: get all products which have been ordered in quantities bigger than 200 and sold in quantities smaller than 5
SELECT DISTINCT P.name, P.price, P.quantity
FROM Products P
WHERE P.PID IN(
SELECT O.PID
FROM OrdersProduct O
WHERE O.quantity > 200
)
INTERSECT
SELECT P.name, P.price, P.quantity
FROM Products P
WHERE P.PID IN (
SELECT S.PID
FROM SaleProducts S
WHERE S.quantity < 5
)

-- select all products of category 'pencils' and that have a discount
SELECT P.name, P.price, P.quantity
FROM Products P, Categories C
WHERE P.CID = C.CID and C.name = 'pencils' AND P.PID IN
(
SELECT P1.PID
FROM Products P1, Promotion Pr
WHERE P1.PID = Pr.PID
)


-- DIFFERENCE with EXCEPT: get all products except the ones sold by Ioana
SELECT P.name
FROM Products P
EXCEPT
SELECT P.name
FROM Products P, Sale S, SaleProducts SP, Employee E
WHERE S.saleID = SP.saleID AND P.PID = SP.PID AND E.EID = S.EID AND E.firstName = 'Ioana'


-- DIFFERENCE with NOT IN: get all employees who have not placed any orders
SELECT DISTINCT E.firstName, E.lastName
FROM Employee E
WHERE E.EID NOT IN
(
SELECT E1.EID
FROM Employee E1, Orders O
WHERE E1.EID = O.EID
)

-- INNER JOIN, joins at least 3 tables: retrieve information about the orders: the products that have been ordered, their supplier and the employee that made the order
SELECT 
	OP.OID,
	OP.PID,
	P.name AS productName,
	S.name AS supplierName,
	E.firstName AS employeeName
FROM OrdersProduct OP
INNER JOIN Products P ON P.PID = OP.PID
INNER JOIN Orders O ON O.OID = OP.OID
INNER JOIN Employee E ON E.EID = O.EID
INNER JOIN Supplier S ON S.SID = O.SID

-- LEFT JOIN: get information about the sales made by each employees
SELECT *
FROM Employee E
LEFT JOIN Sale S ON S.EID = E.EID
LEFT JOIN SaleProducts SP ON SP.saleID = S.saleID
LEFT JOIN Products P ON SP.PID = P.PID

-- RIGHT JOIN: get information about a all categories: what products we have for each category and if they have a discount
SELECT 
	P.name AS productName,
	Pr.discountPercentage AS promotionPercentage,
	P.price AS productPrice,
	P.quantity AS productQuantity,
	C.name AS categoryName
FROM Promotion Pr
RIGHT JOIN Products P ON Pr.PID = P.PID
RIGHT JOIN Categories C ON P.CID = C.CID
ORDER BY P.quantity

-- FULL JOIN: get all information about all aspects related to products: category, details, promotions
SELECT 
	P.name AS productName,
	Pr.discountPercentage AS promotionPercentage,
	P.price AS productPrice,
	P.quantity AS productQuantity,
	C.name AS categoryName,
	D.manufacturer,
	D.description
FROM Products P
FULL JOIN ProductDetails D ON D.PID = P.PID
FULL JOIN Categories C ON C.CID = P.CID
FULL JOIN Promotion Pr ON Pr.PID = P.PID

-- IN operator in WHERE clause and a subclause: select the products which have been sold in a sale in a quantity over 5
SELECT 
	P.PID, 
	P.name AS productName,
	P.price AS prodyctPrice
FROM Products P
WHERE P.PID IN
(
SELECT SP.PID
FROM SaleProducts SP
WHERE SP.quantity > 5
)

-- IN operator in WHERE clause and 2 subclauses: select top 3 products sold by the employee with EID = 2
SELECT TOP 3
	P.PID, 
	P.name AS productName,
	P.price AS prodyctPrice
FROM Products P
WHERE P.PID IN
(
SELECT SP.PID
FROM SaleProducts SP
WHERE SP.saleID IN
(
SELECT S.saleID
FROM Sale S
WHERE S.EID = 2
)
)

-- EXISTS operator and a subquery in the WHERE clause: select all employees that made any sales
SELECT *
FROM Employee E
WHERE EXISTS
(
SELECT * 
FROM Sale S
WHERE E.EID = S.EID
)

-- EXISTS operator and a subquery in the WHERE clause: select all products that have a promotion with a discount percentage over 20
SELECT *
FROM Products P
WHERE EXISTS
(
SELECT *
FROM Promotion Pr
WHERE Pr.PID = P.PID AND Pr.discountPercentage > 20
)

-- subquery in the FROM clause: get all items with a price smaller than the average price
SELECT *
FROM (SELECT AVG(price) AS AveragePrice FROM Products) AS A, Products P
WHERE P.price <= AveragePrice

-- subquery in the FROM clause: select all orders made from suppliers whose phone numbers end in 8
SELECT *
FROM (SELECT * FROM Supplier where phoneNumber LIKE '%8') AS SP, Orders O
WHERE O.SID = SP.SID

-- GROUP BY: select TOP 3 the minimum price of a product, where the products have been gouped by their category
SELECT TOP 3 MIN(P.price) AS minPrice, P.CID
FROM Products P
GROUP BY P.CID

-- GROUP BY with HAVING: get the number of times a product have been sold, where it has been sold for at least 2 times
SELECT COUNT(*) AS timesSold, SP.PID
FROM SaleProducts SP
GROUP BY SP.PID
HAVING COUNT(*) >= 2

-- GROUP BY with HAVING with subquery: get the cost of all orders made at the suppliers Office Supplies or XYZ Supplier 
SELECT SUM(O.amount) AS sumCost, O.SID
FROM Orders O
GROUP BY O.SID
HAVING O.SID IN 
(
SELECT S.SID
FROM Supplier S
WHERE S.SID = O.SID AND (S.name = 'Office Supplies' OR S.name = 'XYZ Supplier')
)

-- GROUP BY with HAVING with subquery: select the average quantity sold from a product having the category 1 or 3
SELECT AVG(SP.quantity) as avgQuantitySale, SP.PID
FROM SaleProducts SP
GROUP BY SP.PID
HAVING SP.PID IN
(
SELECT P.PID
FROM Products P
WHERE P.PID = SP.PID AND (P.CID = 1 OR P.CID = 3)
)

--query using ANY: get all the products that have the price bigger than any products from CID 1
SELECT P.name, P.price, P.quantity, P.price * P.quantity as totalValueProduct
FROM Products P
WHERE P.price > ANY(
	SELECT P2.price
	FROM Products P2
	WHERE P2.CID = 1
)

-- rewrite with aggregation operators
SELECT P.name, P.price, P.quantity,P.price * P.quantity as totalValueProduct
FROM Products P
WHERE P.price > (
	SELECT MIN(P2.price)
	FROM Products P2
	WHERE P2.CID = 1
)

-- query using ANY: get the employees who made any sells
SELECT E.firstName, E.lastName, E.phoneNumber
FROM Employee E
WHERE E.EID = ANY(
SELECT S.EID
FROM Sale S
)

-- rewritten with in
SELECT E.firstName, E.lastName, E.phoneNumber
FROM Employee E
WHERE E.EID IN(
SELECT S.EID
FROM Sale S
)

-- query using ALL: get the employees who have not made any sales
SELECT E.firstName, E.lastName, E.phoneNumber
FROM Employee E
WHERE E.EID <> ALL(
	SELECT S.EID
	FROM Sale S
)

-- rewrite with not in
SELECT E.firstName, E.lastName, E.phoneNumber
FROM Employee E
WHERE E.EID NOT IN(
	SELECT S.EID
	FROM Sale S
)

-- query with ALL: get all the products who have prices bigger than all products made by the first supplier
SELECT DISTINCT P.name, P.price
FROM Products P
WHERE P.price >= ALL(
SELECT price
FROM Products P2
WHERE P2.SID = 1
)

-- rewrite with aggregation
SELECT P.name, P.price, P.quantity, P.price * P.quantity as totalValueProduct
FROM Products P
WHERE P.price >=(
SELECT MAX(price)
FROM Products P2
WHERE P2.SID = 1
)
