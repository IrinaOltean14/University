use Lab1

-- insert into Tables

DROP PROCEDURE IF EXISTS insertIntoTables
GO

CREATE PROCEDURE insertIntoTables (@tableName VARCHAR(60)) AS
BEGIN
	IF @tableName IN
		(
			SELECT Name
			FROM Tables
		)
		BEGIN
			PRINT 'Table already in Tables!'
			RETURN
		END
	INSERT INTO Tables(Name) VALUES (@tableName)
END
GO

-- insert into Views

DROP PROCEDURE IF EXISTS insertIntoViews
GO

CREATE PROCEDURE insertIntoViews (@viewName VARCHAR(60)) AS
BEGIN
	IF @viewName IN
		(
			SELECT Name
			FROM Views
		)
		BEGIN
			PRINT 'View already in Views!'
			RETURN
		END
	INSERT INTO Views(Name) VALUES (@viewName)
END
GO


-- insert into tests
DROP PROCEDURE IF EXISTS insertIntoTests;
GO

CREATE PROCEDURE insertIntoTests (@testName VARCHAR(60), @testID INT) AS
BEGIN
	IF @testName IN (SELECT Name FROM Tests)
	BEGIN
		PRINT 'Test already in Tests!'
		RETURN
	END

	INSERT INTO Tests (Name)
	VALUES (@testName)
END
GO

-- insert into TestTables (connect table to test)
DROP PROCEDURE IF EXISTS connectTableToTest;
GO

CREATE PROCEDURE connectTableToTest (@tableName VARCHAR(60), @testName VARCHAR(60), @nb_of_rows INT, @position INT) AS
BEGIN
	INSERT INTO TestTables(TestID, TableID, NoOfRows, Position) VALUES (
		(SELECT T.TestID FROM Tests T WHERE T.Name = @testName),
		(SELECT TB.TableID FROM Tables TB WHERE TB.name = @tableName),
		@nb_of_rows,
		@position
	)
END 
GO

-- insert into TestViews (connect view to test)
DROP PROCEDURE IF EXISTS connectViewToTest;
GO

CREATE PROCEDURE connectViewToTest (@viewName VARCHAR(60), @testName VARCHAR(60)) AS
BEGIN
	INSERT INTO TestViews(TestID, ViewID) VALUES(
		(SELECT T.TestID FROM Tests T WHERE T.Name = @testName),
		(SELECT V.ViewID FROM Views V WHERE V.Name = @viewName)
	)
END 
GO


-- generate random string
DROP PROCEDURE IF EXISTS generateRandomString
GO

CREATE PROCEDURE generateRandomString (@string VARCHAR(60) OUTPUT) AS
BEGIN
	DECLARE @length INT;
	SET @length = 0;
	DECLARE @limit INT;
	SET @limit = 5 + RAND() * 20;

	SET @string = '';
	WHILE (@length < @limit)
	BEGIN
		SET @string = @string + CHAR((RAND() * 25 + 97));
		SET @length = @length + 1;
	END
END
GO

-- generate random int
DROP PROCEDURE IF EXISTS generateRandomInt;
GO

CREATE PROCEDURE generateRandomInt (@lowLimit INT, @maxLimit INT, @integer INT OUTPUT) AS
BEGIN
	SET @integer = @lowLimit + RAND() * @maxLimit;
END
GO

-- primary key retrieval 
-- to determine whether a specified column in a table is part of the primary key of that table

DROP FUNCTION IF EXISTS isPrimaryKey;
GO

CREATE FUNCTION isPrimaryKey (@table VARCHAR(128), @column VARCHAR(128))
RETURNS INT
AS
BEGIN
	DECLARE @counter INT;
	SET @counter = 0;

	SET @counter = (
		SELECT COUNT(*)
		FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS C
			JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS K ON C.TABLE_NAME = K.TABLE_NAME
															AND C.CONSTRAINT_CATALOG = K.CONSTRAINT_CATALOG
															AND C.CONSTRAINT_SCHEMA = K.CONSTRAINT_SCHEMA
															AND C.CONSTRAINT_NAME = K.CONSTRAINT_NAME
		WHERE C.CONSTRAINT_TYPE = 'PRIMARY KEY' AND K.COLUMN_NAME = @column AND C.TABLE_NAME = @table)
	IF @counter = 0
		BEGIN
			RETURN 0
		END
	RETURN 1
END
GO

-- foreign key retrieval
DROP PROCEDURE IF EXISTS getReferenceData;
GO

CREATE PROCEDURE getReferenceData (@table VARCHAR(128), @column VARCHAR(128), @referencedTable VARCHAR(128) OUTPUT, @referencedColumn VARCHAR(128) OUTPUT)
AS
BEGIN
	SELECT @referencedTable = OBJECT_NAME(FC.referenced_object_id), @referencedColumn = COL_NAME(FC.referenced_object_id, FC.referenced_column_id)
	FROM sys.foreign_keys AS F INNER JOIN sys.foreign_key_columns AS FC ON F.OBJECT_ID = FC.constraint_object_id
	WHERE OBJECT_NAME (F.parent_object_id) = @table AND COL_NAME(FC.parent_object_id, FC.parent_column_id) = @column
END
GO

-- insert a row of data in a given table


DROP PROCEDURE IF EXISTS insertRow;
GO

CREATE PROCEDURE insertRow(@tableName VARCHAR(70)) AS
BEGIN
	DECLARE @getColumnsQuery NVARCHAR(MAX) = N'
		SELECT COLUMN_NAME, DATA_TYPE
		FROM INFORMATION_SCHEMA.COLUMNS
		WHERE TABLE_NAME = ''' + @tableName + '''
	';
	-- holds a dynamic SQL query that retrieves column information (names + data types)

	DECLARE @insertQuery NVARCHAR(MAX) = N'INSERT INTO ' + @tableName;
	-- dynamic SQL statement for the INSERT INTO operation

	DECLARE @columns NVARCHAR(MAX);
	DECLARE @types NVARCHAR(MAX);
	DECLARE @rowsNumber INT = 0;

	-- we use a cursor to extract all columns from the table and their types
	DECLARE @cursorQuery NVARCHAR(MAX) = N'
		DECLARE @columnName NVARCHAR(MAX);
		DECLARE @dataType NVARCHAR(MAX);
		DECLARE columnsCursor CURSOR FOR ' + @getColumnsQuery + '
		OPEN columnsCursor
		FETCH columnsCursor
		INTO @columnName, @dataType;

		IF @@FETCH_STATUS = 0
		BEGIN
			SET @columns = @columnName;
			SET @types = @dataType;
			SET @rowsNumber = 1;
		END

		WHILE @@FETCH_STATUS = 0
		BEGIN
			FETCH columnsCursor
			INTO @columnName, @dataType;
			IF @@FETCH_STATUS = 0
			BEGIN
				SET @columns = @columns + '', '' + @columnName;
				SET @types = @types + '', '' + @dataType;
				SET @rowsNumber = @rowsNumber + 1;
			END
		END

		CLOSE columnsCursor;
		DEALLOCATE columnsCursor;	
	';

	EXEC sp_executesql @Query = @cursorQuery, @Params = N'@columns NVARCHAR(MAX) OUTPUT, @types NVARCHAR(MAX) OUTPUT, @rowsNumber INT OUTPUT', @columns = @columns OUTPUT, @types = @types OUTPUT, @rowsNumber = @rowsNumber OUTPUT;

	SET @insertQuery = @insertQuery + '(' + @columns + ') VALUES (';
	SET @types = @types + ', ';
	SET @columns = @columns + ', ';

	DECLARE @index INT = 0;
	DECLARE @current NVARCHAR(MAX);
	DECLARE @currentColumn NVARCHAR(MAX);
	DECLARE @pkConstraint INT = 0;
	DECLARE @outputPK INT;
	DECLARE @pkQuery NVARCHAR(MAX)

	-- insert random data on every column

	WHILE @index < @rowsNumber
	BEGIN
		SET @current = LEFT(@types, CHARINDEX(', ', @types) -1);
		-- extracts the data type of the first column
		SET @types = SUBSTRING(@types, CHARINDEX(', ', @types) + 2, LEN(@types));
		-- updates types
		SET @currentColumn = LEFT(@columns, CHARINDEX(', ', @columns) - 1);
		SET @columns = SUBSTRING(@columns, CHARINDEX(', ', @columns) + 2, LEN(@columns));
		-- same but for columns

		IF @index != 0
			SET @insertQuery = @insertQuery + ', ';

		DECLARE @referencedTable NVARCHAR(MAX) = '';
		DECLARE @referencedColumn NVARCHAR(MAX) = '';
		
		-- here we check if the current column has a foreign key 
		EXEC getReferenceData @tableName, @currentColumn, @referencedTable = @referencedTable OUTPUT, @referencedColumn = @referencedColumn OUTPUT;

		-- here we check if the current column has a primary key
		SET @pkConstraint = dbo.isPrimaryKey(@tableName, @currentColumn);

		-- case 1: we must insert a integer
		IF @current = 'INT'
		BEGIN
			-- case 1.1: it's a foreign key => we must search in the refferenced table
			IF @referencedTable != '' AND @referencedColumn != ''
			BEGIN
				DECLARE @intValue INT;
				DECLARE @intQuery NVARCHAR(MAX) = N'
					SELECT TOP 1 @intValue = ' + @referencedColumn + ' FROM ' + @referencedTable+ ' ORDER BY NEWID() ';
				--PRINT @intQuery
				EXEC sp_executesql @Query = @intQuery, @Params = N'@intValue INT OUTPUT', @intValue = @intValue OUTPUT;
				SET @insertQuery = @insertQuery + CONVERT(NVARCHAR(MAX), @intValue);
			END
			ELSE
			BEGIN
				DECLARE @integer INT;
				-- case 1.2: it's a primary key => we generate a random value and we must check if the value doesn't already exist
				IF @pkConstraint = 1
				BEGIN
					EXEC generateRandomInt 0, 1000, @integer = @integer OUTPUT;
					SET @pkQuery = N'SELECT @outputPK = COUNT (*) FROM ' + @tableName + ' WHERE '	+ @currentColumn + '=' + CONVERT(NVARCHAR(MAX), @integer);
					EXEC sp_executesql @pkQuery, N'@outputPK INT OUTPUT', @outputPK OUTPUT
					PRINT @outputPK
					IF @outputPK != NULL
					BEGIN
						WHILE @outputPK != NULL 
						BEGIN
							SET @pkQuery = N'SELECT @outputPK = COUNT (*) FROM ' + @tableName + ' WHERE '	+ @currentColumn + '=' + CONVERT(NVARCHAR(MAX), @integer);
							EXEC sp_executesql @pkQuery, N'@outputPK INT OUTPUT', @outputPK OUTPUT
						END
					END
					SET @insertQuery = @insertQuery + CONVERT(NVARCHAR(MAX), @integer);
				END
				-- case 1.3: it's not a foreign key or a primary key => we insert a random value
				ELSE
				BEGIN
					EXEC generateRandomInt 0, 1000, @integer = @integer OUTPUT;
					SET @insertQuery = @insertQuery + CONVERT(NVARCHAR(MAX), @integer);
				END

			END
		END
		-- case 2: we must insert a string
		IF @current = 'VARCHAR'
		BEGIN
			-- case 2.1: it's a foreign key => we must search in the refferenced table
			IF @referencedTable != '' AND @referencedColumn != ''
			BEGIN
				DECLARE @stringValue NVARCHAR(MAX);
				DECLARE @stringQuery NVARCHAR(MAX) = N'
					SELECT TOP 1 @stringValue = ' + @referencedColumn + ' FROM ' + @referencedTable + ' ORDER BY NEWID() ';
				EXEC sp_executesql @Query = @stringQuery, @Params = N'@stringValue INT OUTPUT', @stringValue = @stringValue OUTPUT;
				SET @insertQuery = @insertQuery + CONVERT(NVARCHAR(MAX), @stringValue);
			END
			ELSE 
			BEGIN
				DECLARE @string NVARCHAR(21);
				-- case 2.2: it's a primary key => we generate a random value and we must check if the value doesn't already exist
				IF @pkConstraint = 1
				BEGIN
					EXEC generateRandomString @string = @string OUTPUT;
					SET @pkQuery = N'SELECT @outputPK = COUNT (*) FROM ' + @tableName + ' WHERE '	+ @currentColumn + '=' + @string;
					EXEC sp_executesql @pkQuery, N'@outputPK VARCHAR OUTPUT', @outputPK OUTPUT;
					PRINT @outputPK;
					IF @outputPK != NULL
					BEGIN
						WHILE @outputPK != NULL 
						BEGIN
							SET @pkQuery = N'SELECT @outputPK = COUNT (*) FROM ' + @tableName + ' WHERE '	+ @currentColumn + '=' + @string;
							EXEC sp_executesql @pkQuery, N'@outputPK VARCHAR OUTPUT', @outputPK OUTPUT;
						END
					END
					SET @insertQuery = @insertQuery + '''' + @string + '''';
				END
				-- case 2.3: it's not a foreign key or a primary key => we insert a random value
				ELSE
				BEGIN
					EXEC generateRandomString @string = @string OUTPUT;
					SET @insertQuery = @insertQuery + '''' + @string + '''';
				END
			END
		END

		SET @index = @index + 1;
	END

	SET @insertQuery = @insertQuery + ');';
	PRINT @insertQuery;
	EXEC sp_executesql @insertQuery;
END
GO

-- insert multiple rows of data in a given table
DROP PROCEDURE IF EXISTS insertMultipleRows;
GO

CREATE PROCEDURE insertMultipleRows (@tableName VARCHAR(70), @nb INT) AS
BEGIN
	WHILE @nb > 0
	BEGIN
		DECLARE @error INT = 1;
		WHILE @error != 0
		BEGIN
			SET @error = 0;
			BEGIN TRY
				EXEC insertRow @tableName;
			END TRY
			BEGIN CATCH
				SET @error = 1;
			END CATCH
		END

		SET @nb = @nb - 1;
	END
END 
GO

-- run test procedure
DROP PROCEDURE IF EXISTS runTest;
GO

CREATE PROCEDURE runTest (@testID INT) AS
BEGIN
	DECLARE @tests INT = 0;
	DECLARE @tableID INT = -1;
	DECLARE @viewID INT = -1;
	DECLARE @rowsNb INT = -1;
	DECLARE @runID INT = -1;
	DECLARE @testStart DATETIME = GETDATE();

	INSERT INTO TestRuns (Description, StartAt)
	VALUES ((SELECT Name FROM Tests WHERE TestID = @testID), @testStart);

	SELECT @runID = TestRunID FROM TestRuns 
	WHERE Description = (SELECT Name FROM Tests WHERE TestID = @testID) AND StartAt = @testStart;

	SELECT @tests = COUNT(*) FROM Tests
	WHERE TestID = @testID;

	IF @testID < 0
	BEGIN
		RAISERROR('Invalid test ID!', 10, 1);
		RETURN
	END

	-- run test for tables --

	DECLARE @tableName NVARCHAR(MAX);
	DECLARE @query NVARCHAR(MAX);

	-- first we delete data from the tables --

	DECLARE testCursor CURSOR FOR
	SELECT TableID FROM TestTables
	WHERE TestID = @testID
	ORDER BY Position DESC;

	OPEN testCursor
	FETCH testCursor
	INTO @tableId;

	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @tableName = Name FROM Tables
		WHERE TableID = @tableID;

		SET @query = N'DELETE FROM ' + @tableName;
		EXEC sp_executesql @query;

		FETCH testCursor
		INTO @tableId;
	END

	CLOSE testCursor
	DEALLOCATE testCursor

	-- now we insert data to tables --
	
	DECLARE testCursor CURSOR FOR
	SELECT TableID, NoOfRows FROM TestTables
	WHERE TestID = @testID
	ORDER BY Position;

	OPEN testCursor
	FETCH testCursor
	INTO @tableId, @rowsNb;

	DECLARE @startInsert DATETIME;
	DECLARE @endInsert DATETIME;

	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @tableName = Name FROM Tables
		WHERE TableID = @tableID;

		SET @startInsert = GETDATE();
		EXEC insertMultipleRows @tableName, @rowsNb;
		SET @endInsert = GETDATE();

		INSERT INTO TestRunTables (TestRunID, TableID, StartAt, EndAt)
		VALUES (@runID, @tableID, @startInsert, @endInsert)

		FETCH testCursor
		INTO @tableID, @rowsNb;
	END

	CLOSE testCursor
	DEALLOCATE testCursor

	-- run test for views --

	DECLARE @viewName NVARCHAR(MAX);

	DECLARE testCursor CURSOR FOR
	SELECT ViewID FROM TestViews
	WHERE TestID = @testID

	OPEN testCursor
	FETCH testCursor 
	INTO @viewID;

	DECLARE @startView DATETIME;
	DECLARE @endView DATETIME;

	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @viewName = Name FROM Views
		WHERE ViewID = @viewID;

		SET @query = 'SELECT * FROM ' + @viewName;

		SET @startView = GETDATE();
		EXEC sp_executesql @query;
		SET @endView = GETDATE();

		INSERT INTO TestRunViews (TestRunID, ViewID, StartAt, EndAt)
		VALUES (@runID, @viewID, @startView, @endView);

		FETCH testCursor
		INTO @viewID;
	END

	CLOSE testCursor;
	DEALLOCATE testCursor;

	-- set TestRuns table data --
	UPDATE TestRuns
	SET EndAt = GETDATE()
	WHERE Description = (SELECT Name FROM Tests WHERE TestID = @testID) AND StartAt = @testStart;

END 
GO

-- a view with a SELECT statement operating on one table

CREATE OR ALTER VIEW suppliersNameC
AS 
	SELECT *
	FROM Supplier
	WHERE name LIKE 'C%';
GO

-- a view with a SELECT statement that operates on at least 2 different tables and contains at least 1 JOIN operator
CREATE OR ALTER VIEW productInfo
AS
	SELECT P.name AS productName, C.name AS category
	FROM Products P
	INNER JOIN Categories C ON P.CID = C.CID
GO

-- a view with a SELECT statement that has a GROUP BY clause, operates on at least 2 different tables and contains at least one JOIN operator.
CREATE OR ALTER VIEW ordersDetails
AS
	SELECT P.name AS name, SUM(OP.quantity) AS totalQuantity
	FROM OrdersProduct OP
		INNER JOIN Orders O ON OP.OID = O.OID
		INNER JOIN Products P ON P.PID = OP.PID
	GROUP BY P.name
GO

-- a table with a single column primary key and no foreign keys: Supplier
EXEC insertIntoViews 'suppliersNameC'
EXEC insertIntoTests 'test1', 1
EXEC insertIntoTables 'Supplier'
EXEC connectTableToTest 'Supplier', 'test1', 5, 1
EXEC connectViewToTest 'suppliersNameC', 'test1'

-- a table with a single column primary key and at least one foreign key: Sale
EXEC insertIntoViews 'productInfo'
EXEC insertIntoTests 'test2', 2
EXEC insertIntoTables 'Categories'
EXEC insertIntoTables 'Products'
EXEC connectTableToTest 'Categories', 'test2', 5, 1
EXEC connectTableToTest 'Products', 'test2', 5, 2
EXEC connectViewToTest 'productInfo', 'test2'

-- a table with a multicolumn primary key: OrderProducts
EXEC insertIntoViews 'ordersDetails'
EXEC insertIntoTests 'test3', 3
EXEC insertIntoTables 'Orders'
EXEC insertIntoTables 'OrdersProduct'
EXEC connectTableToTest 'Orders', 'test3', 5, 1
EXEC connectTableToTest 'Products', 'test3', 5, 2
EXEC connectTableToTest 'OrdersProduct', 'test3', 5, 3
EXEC connectViewToTest 'ordersDetails', 'test3'

EXEC runTest 2;

SELECT * FROM TestTables
SELECT * FROM TestViews
SELECT * FROM TestRuns
SELECT * FROM TestRunTables
SELECT * FROM TestRunViews





