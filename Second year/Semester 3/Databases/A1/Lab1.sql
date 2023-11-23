CREATE DATABASE Lab1

USE Lab1

CREATE TABLE Supplier(
	SID int not null, 
	name varchar(255),
	phoneNumber varchar(15),
	primary key(SID)
)

select * from Supplier
INSERT INTO Supplier(SID, name, phoneNumber) values (1, 'Office Supplies', '074* *** ***')
INSERT INTO Supplier(SID, name, phoneNumber) values (2, 'XYZ Supplier', '074* *** ***')
INSERT INTO Supplier(SID, name, phoneNumber) values (3, 'IPB', '074* *** ***')


CREATE TABLE Categories(
	CID int not null,
	name varchar(255) not null,
	primary key(CID)
)

select * from Categories
INSERT INTO Categories(CID, name) values (1, 'paper')
INSERT INTO Categories(CID, name) values (2, 'pens')
INSERT INTO Categories(CID, name) values (3, 'pencils')

CREATE TABLE Products(
	PID int not null, 
	name varchar(255) not null,
	SID int not null,
	CID int not null,
	price int not null, 
	quantity int not null,
	primary key(PID),
	foreign key (SID) references Supplier(SID) on delete cascade,
	foreign key (CID) references Categories(CID) on delete cascade
)

select * from Products
INSERT INTO Products(PID, name, SID, CID, price, quantity) values (1, 'Colored pencils', 1, 3, 30, 100)
INSERT INTO Products(PID, name, SID, CID, price, quantity) values (2, 'White Paper', 2, 1, 5, 200)
INSERT INTO Products(PID, name, SID, CID, price, quantity) values (3, 'Blue pen', 3, 2, 2, 250)


CREATE TABLE ProductDetails(
	PID int not null,
	description varchar(255),
	manufacturer varchar(255),
	primary key(PID),
	foreign key (PID) references Products(PID) on delete cascade
)

select * from ProductDetails
INSERT INTO ProductDetails(PID, description, manufacturer) values (1, '12 pencils in different colors', 'Faber Castle')
INSERT INTO ProductDetails(PID, description, manufacturer) values (2, 'pack of 100 sheets of paper', 'Ecada')
INSERT INTO ProductDetails(PID, description, manufacturer) values (3, 'Pen with blue ink, refillable', 'Daco')


CREATE TABLE Employee(
	EID int not null,
	firstName varchar(255) not null,
	lastName varchar(255) not null,
	salary int not null,
	phoneNumber varchar(15) not null,
	primary key(EID)
)

select * from Employee
INSERT INTO Employee(EID, firstName, lastName, salary, phoneNumber) values (1, 'Maria', 'Pop', 3500, '07** *** ***')
INSERT INTO Employee(EID, firstName, lastName, salary, phoneNumber) values (2, 'Mihai', 'Ionescu', 2500, '07** *** ***')
INSERT INTO Employee(EID, firstName, lastName, salary, phoneNumber) values (3, 'Ioana', 'Sabo', 3000, '07** *** ***')

CREATE TABLE Sale(
	saleID int not null,
	saleDate date not null,
	EID int not null,
	primary key(saleID),
	foreign key (EID) references Employee(EID)
)
select * from Sale
INSERT INTO Sale(saleID, saleDate, EID) values (1, '2023-10-01', 2)
INSERT INTO Sale(saleID, saleDate, EID) values (2, '2023-10-02', 3)
INSERT INTO Sale(saleID, saleDate, EID) values (3, '2023-10-03', 2)

CREATE TABLE SaleProducts(
	saleID int not null,
	PID int not null,
	quantity int not null,
	primary key(saleID, PID),
	foreign key(saleID) references Sale(saleID),
	foreign key (PID) references Products(PID)
)
select * from SaleProducts
INSERT INTO SaleProducts(saleID, PID, quantity) values (1, 1, 2)
INSERT INTO SaleProducts(saleID, PID, quantity) values (1, 2, 1)
INSERT INTO SaleProducts(saleID, PID, quantity) values (2, 1, 5)
INSERT INTO SaleProducts(saleID, PID, quantity) values (2, 3, 6)
INSERT INTO SaleProducts(saleID, PID, quantity) values (3, 3, 10)

ALTER TABLE SaleProducts
ADD CONSTRAINT x
FOREIGN KEY (PID)
REFERENCES Products(PID)
ON DELETE CASCADE

CREATE TABLE Promotion(
	PID int not null,
	discountPercentage int not null,
	primary key(PID),
	foreign key(PID) references Products(PID) on delete cascade
)
select * from Promotion
INSERT INTO Promotion(PID, discountPercentage) values (1, 20)

CREATE TABLE Orders(
	OID int not null,
	SID int not null,
	EID int not null,
	orderDate date not null,
	amount int not null,
	primary key (OID),
	foreign key (SID) references Supplier(SID),
	foreign key (EID) references Employee(EID)
)
select * from Orders
INSERT INTO Orders(OID, SID, EID, orderDate, amount) values (1,1,2,'2023-09-25', 5000)
INSERT INTO Orders(OID, SID, EID, orderDate, amount) values (2,2,2,'2023-09-26', 2000)
INSERT INTO Orders(OID, SID, EID, orderDate, amount) values (3,3,2,'2023-09-27', 3000)
INSERT INTO Orders(OID, SID, EID, orderDate, amount) values (4,4,1,'2023-09-27', 3000)

CREATE TABLE OrdersProduct(
	OID int not null,
	PID int not null,
	quantity int not null,
	primary key (OID, PID),
	foreign key (OID) references Orders(OID),
	foreign key (PID) references Products(PID)
)
select * from OrdersProduct
INSERT INTO OrdersProduct(OID, PID, quantity) values (1, 3, 100)
INSERT INTO OrdersProduct(OID, PID, quantity) values (1, 2, 200)
INSERT INTO OrdersProduct(OID, PID, quantity) values (2, 2, 1000)
INSERT INTO OrdersProduct(OID, PID, quantity) values (2, 1, 500)
INSERT INTO OrdersProduct(OID, PID, quantity) values (3, 3, 2000)

ALTER TABLE OrdersProduct
ADD CONSTRAINT y
FOREIGN KEY (PID)
REFERENCES Products(PID)
ON DELETE CASCADE