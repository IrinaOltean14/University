use Lab1
GO

-- a. modify the type of a column
-- modify product price from INT to TINYINT
CREATE OR ALTER PROCEDURE setProductPriceToTinyInt -- allows you to create a stored procedure if it does not already exist or alter (modify) it if it already exists
AS
	ALTER TABLE Products
		ALTER COLUMN price TINYINT
GO


-- a. undo
-- modify product price from TINYINT to INT
CREATE OR ALTER PROCEDURE setProductPriceToInt
AS
	ALTER TABLE Products
		ALTER COLUMN price INT
GO

-- b. add/remove column
-- add review to product
CREATE OR ALTER PROCEDURE addReviewProduct
AS
	ALTER TABLE Products
		ADD review INT DEFAULT 0 
GO

-- b. undo
-- remove column review from Products table
CREATE OR ALTER PROCEDURE removeReviewProduct
AS
BEGIN
    -- Drop the default constraint
    DECLARE @defaultConstraintName NVARCHAR(128)

    SELECT @defaultConstraintName = name
    FROM sys.default_constraints
    WHERE parent_object_id = OBJECT_ID('Products')
      AND col_name(parent_object_id, parent_column_id) = 'review'

    IF @defaultConstraintName IS NOT NULL
    BEGIN
        DECLARE @sql NVARCHAR(MAX)
        SET @sql = 'ALTER TABLE Products DROP CONSTRAINT ' + QUOTENAME(@defaultConstraintName)
        EXEC sp_executesql @sql
    END

    -- Remove the column
    ALTER TABLE Products
    DROP COLUMN IF EXISTS review
END
GO


-- c. add/remove DEFAULT constraint
-- add default phone number in table Supplier
CREATE OR ALTER PROCEDURE addDefaultNumber
AS
	ALTER TABLE Supplier
		ADD CONSTRAINT default_number
			DEFAULT '074* *** ***' for phoneNumber
GO

-- c.undo
-- remove default constraint for salary
CREATE OR ALTER PROCEDURE removeDefaultNumber
AS
	ALTER TABLE Supplier
		DROP CONSTRAINT IF EXISTS default_number
GO


-- g. create/drop a table
-- create table 
-- create table CLIENT
CREATE OR ALTER PROCEDURE addTableClient
AS
	CREATE TABLE Client(
		CLID INT not null,
		name VARCHAR(50),
		SaleID INT,
	)
GO

-- g. undo
CREATE OR ALTER PROCEDURE dropTableClient
AS
	DROP TABLE IF EXISTS Client
GO

-- d. add/remove a primary key
-- add to table Client the primary key CLID
CREATE OR ALTER PROCEDURE addPrimaryKeyDiscount
AS
	ALTER TABLE Client
		ADD CONSTRAINT primary_key PRIMARY KEY(CLID)
GO

-- d.undo
CREATE OR ALTER PROCEDURE removePrimaryKeyDiscount
AS
	ALTER TABLE Client
		DROP CONSTRAINT IF EXISTS primary_key
GO


-- e. add/remove a candidate key
-- a candidate key is a set of one or more columns in a relational database table that can uniquely identify each record in the table
-- for Employee table add candidate key phoneNumber
CREATE OR ALTER PROCEDURE addCandidateKeyEmployee
AS
	ALTER TABLE Employee
		ADD CONSTRAINT nb_ck UNIQUE (firstName, lastName, phoneNumber)
GO

-- e.undo
CREATE OR ALTER PROCEDURE removeCandidateKeyEmployee
AS
	ALTER TABLE Employee
		DROP CONSTRAINT IF EXISTS nb_ck
GO


-- f. add/remove a foreign key
-- add SID (Supplier ID) as a foreign key to Orders table
CREATE OR ALTER PROCEDURE addForeignKey
AS
	ALTER TABLE Orders
		ADD CONSTRAINT fk_supplierID
				FOREIGN KEY(SID) REFERENCES Supplier(SID) ON DELETE CASCADE
GO

-- f. undo
CREATE OR ALTER PROCEDURE removeForeignKey
AS
	ALTER TABLE Orders
		DROP CONSTRAINT IF EXISTS fk_supplierID
GO


-- table: procedure_name versionFrom versionTo
CREATE TABLE Previous_Versions(
	storedProcedure VARCHAR(50),
	versionFrom INT,
	versionTo INT,
	primary key(versionFrom, versionTo)
)
GO

-- table that keeps the current version
CREATE TABLE Current_Version(
	currentVersion INT DEFAULT 0
)
GO

INSERT INTO Current_Version(currentVersion) VALUES (0)
GO

INSERT INTO Previous_Versions(versionFrom, versionTo, storedProcedure)
VALUES
(0,1,'setProductPriceToTinyInt'),
(1,0,'setProductPriceToInt'),
(1,2,'addReviewProduct'),
(2,1,'removeReviewProduct'),
(2,3,'addDefaultNumber'),
(3,2,'removeDefaultNumber'),
(3,4,'addTableClient'),
(4,3,'dropTableClient'),
(4,5,'addPrimaryKeyDiscount'),
(5,4,'removePrimaryKeyDiscount'),
(5,6,'removeForeignKey'),
(6,5,'addForeignKey'),
(6,7,'addCandidateKeyEmployee'),
(7,6,'removeCandidateKeyEmployee');
GO


CREATE OR ALTER PROCEDURE goToVersion(@newVersion INT) 
AS
	DECLARE @curr INT
	DECLARE @procedureName VARCHAR(100)
	SELECT @curr = currentVersion FROM Current_Version

	IF  @newVersion > (SELECT MAX(versionTo) FROM Previous_Versions) OR @newVersion < 0
		RAISERROR ('Bad version', 10, 1)
	ELSE
	BEGIN
		IF @newVersion = @curr
			PRINT('Already on this version!');
		ELSE
		BEGIN
			IF @curr > @newVersion
			BEGIN
				WHILE @curr > @newVersion
				BEGIN
					SELECT @procedureName = storedProcedure FROM Previous_Versions
					WHERE versionFrom = @curr AND versionTo = @curr - 1
					PRINT('executing: ' + @procedureName);
					EXEC(@procedureName)
					SET @curr = @curr - 1
				END
			END

			IF @curr < @newVersion
			BEGIN
				WHILE @curr < @newVersion
					BEGIN
						SELECT @procedureName = storedProcedure FROM Previous_Versions
						WHERE versionFrom = @curr AND versionTo = @curr + 1
						PRINT('executing: ' + @procedureName);
						EXEC (@procedureName)
						SET @curr = @curr + 1
					END
			END

			UPDATE Current_Version SET currentVersion = @newVersion
		END
	END
GO







