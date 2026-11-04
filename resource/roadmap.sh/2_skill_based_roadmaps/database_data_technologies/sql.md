# SQL

## Metadata
- Type: Skill
- Domain: Database & Data Systems
- Source: roadmap.sh
- Source URL: https://roadmap.sh/sql
- Related Roles:
  - PostgreSQL DBA
  - Backend Developer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Learn the Basics
- **What are Relational Databases?**
  - Relational databases organize data into tables, where each table represents a specific type of entity (like customers or products). These tables are linked together based on relationships between the data, often using shared columns called keys.
- **RDBMS Benefits and Limitations**
  - Relational Database Management Systems (RDBMS) organize data into tables with rows and columns, establishing relationships between these tables using keys. This structured approach offers benefits like data integrity through constraints and ACID properties (Atomicity, Consistency, Isolation, Durability), ensuring reliable transactions.
- **SQL vs NoSQL Databases**
  - SQL (relational) and NoSQL (non-relational) databases represent two different approaches to data storage and retrieval. SQL databases use structured schemas and tables, emphasizing data integrity and complex queries through joins.

### 1.2 Basic SQL Syntax
- **SQL Keywords**
  - SQL keywords are reserved words that have special meanings within SQL statements. These include commands (like SELECT, INSERT, UPDATE), clauses (such as WHERE, GROUP BY, HAVING), and other syntax elements that form the structure of SQL queries.
- **Data Types**
  - SQL data types define the kind of values that can be stored in a column and determine how the data is stored, processed, and retrieved. Common data types include numeric types (INTEGER, DECIMAL), character types (CHAR, VARCHAR), date and time types (DATE, TIMESTAMP), binary types (BLOB), and boolean types.
- **Operators**
  - SQL operators are symbols or keywords used to perform operations on data within a database. They are essential for constructing queries that filter, compare, and manipulate data.
- **SELECT**
  - SELECT is one of the most fundamental SQL commands, used to retrieve data from one or more tables in a database. It allows you to specify which columns to fetch, apply filtering conditions, sort results, and perform various operations on the data.
- **INSERT**
  - The INSERT statement in SQL is used to add new rows of data into a table. It specifies the table to which you want to add data, and the values you want to insert into each column of that table.
- **UPDATE**
  - The UPDATE statement modifies existing data within a table. It allows you to change the values of one or more columns for specific rows based on a specified condition.
- **DELETE**
  - The DELETE statement removes rows from a table. You specify which table to remove data from and can use a WHERE clause to filter which rows should be deleted based on specific conditions.

### 1.3 Data Definition Language (DDL)
- **Truncate Table**
  - Truncate Table is a command in SQL used to remove all rows from a table. It's like resetting the table to its initial, empty state.
- **Alter Table**
  - The ALTER TABLE statement in SQL is used to modify the structure of an existing table. This includes adding, dropping, or modifying columns, changing the data type of a column, setting default values, and adding or dropping primary or foreign keys.
- **Create Table**
  - CREATE TABLE is an SQL statement used to define and create a new table in a database. It specifies the table name, column names, data types, and optional constraints such as primary keys, foreign keys, and default values.
- **Drop Table**
  - The DROP TABLE statement removes a table and its data entirely from a database. It's a permanent operation; once a table is dropped, its structure and all the data it contained are lost unless you have a backup.

### 1.4 Data Manipulation Language (DML)
- **Select**
  - The SELECT statement in SQL is used to retrieve data from one or more tables. It allows you to specify which columns you want to see and apply conditions to filter the rows returned.
- **FROM**
  - The FROM clause in SQL specifies the table or tables from which you're retrieving data. It tells the database which dataset to look at when executing your query.
- **WHERE**
  - The WHERE clause is a fundamental part of the SELECT statement in SQL. It filters the rows returned by a query based on a specified condition.
- **JOINs**
  - SQL JOINs let you combine data from two or more tables based on a related column between them. Think of it as linking information together to get a more complete view.

### 1.5 Aggregate Queries
- **GROUP BY**
  - GROUP BY is an SQL clause used in SELECT statements to arrange identical data into groups. It's typically used with aggregate functions (like COUNT, SUM, AVG) to perform calculations on each group of rows.
- **SUM**
  - SUM is an aggregate function in SQL used to calculate the total of a set of values. It's commonly used with numeric columns in combination with GROUP BY clauses to compute totals for different categories or groups within the data.
- **COUNT**
  - COUNT is an SQL aggregate function that returns the number of rows that match the specified criteria. It can be used to count all rows in a table, non-null values in a specific column, or rows that meet certain conditions when combined with a WHERE clause.
- **AVG**
  - The AVG() function in SQL is an aggregate function that calculates the average value of a numeric column. It returns the sum of all the values in the column, divided by the count of those values.
- **MIN**
  - MIN is an aggregate function in SQL that returns the lowest value in a set of values. It works with numeric, date, or string data types, selecting the minimum value from a specified column.
- **MAX**
  - MAX is an aggregate function in SQL that returns the highest value in a set of values. It can be used with numeric, date, or string data types, selecting the maximum value from a specified column.
- **HAVING**
  - The HAVING clause in SQL is used to filter the results of aggregate functions. It's similar to the WHERE clause, but operates on grouped rows produced by the GROUP BY clause.

---

## 2. Intermediate

### 2.1 Data Constraints
- **ORDER BY**
  - The ORDER BY clause in SQL is used to sort the result set of a query by one or more columns. By default, the sorting is in ascending order, but you can specify descending order using the DESC keyword.
- **HAVING**
  - HAVING is a clause in SQL that filters the results of a GROUP BY query. It's like a WHERE clause, but it operates on groups rather than individual rows.
- **INSERT**
  - INSERT is a SQL command used to add new rows of data into a table. It specifies which table to add the data to and provides the values for each column in the new row.
- **UPDATE**
  - The UPDATE statement modifies existing data within a table. It allows you to change the values of one or more columns in a table, based on specified conditions.
- **DELETE**
  - The DELETE statement in SQL removes existing records from a table. You specify which table to affect and can optionally include a WHERE clause to specify conditions for which rows should be deleted.
- **Primary Key**
  - A primary key in SQL is a unique identifier for each record in a database table. It ensures that each row in the table is uniquely identifiable, meaning no two rows can have the same primary key value.
- **Foreign Key**
  - A foreign key in SQL is a column or group of columns in one table that refers to the primary key of another table. It establishes a link between two tables, enforcing referential integrity and maintaining relationships between related data.
- **Unique**
  - A unique constraint ensures that all values in a column (or a group of columns) are different. It prevents duplicate entries, maintaining data integrity by enforcing uniqueness for the specified field(s).
- **NOT NULL**
  - The NOT NULL constraint in SQL ensures that a column does not accept null values. When a column is defined with this constraint, every row in the table must have a value for that specific column.
- **CHECK**
  - A CHECK constraint in SQL is used to enforce data integrity by specifying a condition that must be true for each row in a table. It allows you to define custom rules or restrictions on the values that can be inserted or updated in one or more columns.

### 2.2 JOIN Queries
- **INNER JOIN**
  - INNER JOINs combine rows from two or more tables based on a related column. They return only the rows where there is a match in the specified columns of all tables involved in the join.
- **LEFT JOIN**
  - A LEFT JOIN returns all rows from the left table (the table listed before the LEFT JOIN keyword) and the matching rows from the right table (the table listed after the LEFT JOIN keyword). If there is no match in the right table for a row in the left table, the result will contain NULL values for the columns from the right table.
- **RIGHT JOIN**
  - A RIGHT JOIN combines rows from two tables based on a related column. It returns all rows from the right table (the table specified after the RIGHT JOIN keyword), and the matching rows from the left table.
- **FULL OUTER JOIN**
  - A FULL OUTER JOIN in SQL combines the results of both LEFT and RIGHT OUTER JOINs. It returns all rows from both tables, matching records where the join condition is met and including unmatched rows from both tables with NULL values in place of missing data.
- **FLOOR**
  - FLOOR is a numeric function that returns the largest integer value that is less than or equal to a given number. Effectively, it rounds a number down to the nearest whole number.
- **ABS**
  - The ABS() function in SQL returns the absolute value of a given numeric expression, meaning it converts any negative number to its positive equivalent while leaving positive numbers unchanged. This function is useful when you need to ensure that the result of a calculation or a value stored in a database column is non-negative, such as when calculating distances, differences, or other metrics where only positive values make sense.
- **MOD**
  - The MOD function in SQL calculates the remainder when one number is divided by another. It takes two arguments: the dividend and the divisor.
- **ROUND**
  - The ROUND function in SQL is used to round a numeric value to a specified number of decimal places. It takes two arguments: the number to be rounded and the number of decimal places to round to.
- **CEILING**
  - The CEILING() function in SQL returns the smallest integer greater than or equal to a given numeric value. It's useful when you need to round up a number to the nearest whole number, regardless of whether the number is already an integer or a decimal.

### 2.3 Subqueries
- **Scalar**
  - A scalar value is a single data item, as opposed to a set or array of values. Scalar subqueries are queries that return exactly one column and one row, often used in SELECT statements, WHERE clauses, or as part of expressions.
- **Column**
  - In SQL, columns are used to categorize the data in a table. A column serves as a structure that stores a specific type of data (ints, str, bool, etc.) in a table.
- **Row**
  - In SQL, a row (also called a record or tuple) represents a single, implicitly structured data item in a table. Each row contains a set of related data elements corresponding to the table's columns.
- **Table**
  - A table is a fundamental structure for organizing data in a relational database. It consists of rows (records) and columns (fields), representing a collection of related data entries.
- **Nested Subqueries**
  - Nested subqueries are queries embedded within another SQL query. Think of it as a query inside a query, where the inner query's result is used by the outer query.
- **Correlated Subqueries**
  - In SQL, a correlated subquery is a subquery that uses values from the outer query in its WHERE clause. The correlated subquery is evaluated once for each row processed by the outer query.

### 2.4 Advanced Functions
- **CONCAT**
  - CONCAT is an SQL function used to combine two or more strings into a single string. It takes multiple input strings as arguments and returns a new string that is the concatenation of all the input strings in the order they were provided.
- **LENGTH**
  - The LENGTH function in SQL returns the number of characters in a string. It's used to measure the size of text data, which can be helpful for data validation, formatting, or analysis.
- **SUBSTRING**
  - SUBSTRING is a SQL function used to extract a portion of a string. It allows you to specify the starting position and length of the substring you want to extract.
- **REPLACE**
  - The REPLACE function in SQL is used to substitute all occurrences of a specified substring within a string with a new substring. It takes three arguments: the original string, the substring to be replaced, and the substring to replace it with.

### 2.5 Views
- **UPPER**
  - UPPER is a string function that transforms all characters in a given string to uppercase. It accepts a single string or character-based column as an argument and returns a new string where every letter has been converted to its uppercase equivalent.
- **LOWER**
  - The LOWER function in SQL converts all characters in a specified string to lowercase. It's a string manipulation function that takes a single argument (the input string) and returns the same string with all alphabetic characters converted to their lowercase equivalents.
- **CASE**
  - The CASE statement in SQL is used to create conditional logic within a query, allowing you to perform different actions based on specific conditions. It operates like an if-else statement, returning different values depending on the outcome of each condition.
- **COALESCE**
  - COALESCE is an SQL function that returns the first non-null value in a list of expressions. It's commonly used to handle null values or provide default values in queries.
- **DATE**
  - The DATE data type in SQL is used to store calendar dates (typically in the format YYYY-MM-DD). It represents a specific day without any time information.
- **TIME**
  - The TIME data type in SQL is used to store time values, typically in the format of hours, minutes, and seconds. It's useful for recording specific times of day without date information.
- **TIMESTAMP**
  - A TIMESTAMP is a data type used to store a specific point in time, typically including both date and time components. It often includes fractions of a second (milliseconds or microseconds) for greater precision.
- **DATEADD**
  - DATEADD is an SQL function used to add or subtract a specified time interval to a date or datetime value. It typically takes three arguments: the interval type (e.g., day, month, year), the number of intervals to add or subtract, and the date to modify.
- **Creating Views**
  - Creating views in SQL involves using the CREATE VIEW statement to define a virtual table based on the result of a SELECT query. Views don't store data themselves but provide a way to present data from one or more tables in a specific format.
- **Modifying Views**
  - Modifying views in SQL allows you to alter the structure or definition of an existing view without having to drop and recreate it. This can involve changing the columns included in the view, updating the underlying tables or conditions used in the view's query, or renaming the view.
- **Dropping Views**
  - Dropping views in SQL involves using the DROP VIEW statement to remove an existing view from the database. This operation permanently deletes the view definition, but it doesn't affect the underlying tables from which the view was created.

### 2.6 Indexes
- **Self Join**
  - A self join is a query in SQL that joins a table to itself. This is useful when you want to compare rows within the same table, often based on a hierarchical relationship or other connection between the data points within that table.
- **Cross Join**
  - A Cross Join produces a result set that is the number of rows in the first table multiplied by the number of rows in the second table. If a WHERE clause is used in conjunction with a CROSS JOIN, it functions like an INNER JOIN.
- **NULLIF**
  - NULLIF is an SQL function that compares two expressions and returns NULL if they are equal, otherwise it returns the first expression. It's particularly useful for avoiding division by zero errors or for treating specific values as NULL in calculations or comparisons.
- **Managing Indexes**
  - Managing indexes in SQL involves creating, modifying, and dropping indexes to optimize database performance. This process includes identifying columns that benefit from indexing (frequently queried or used in JOIN conditions), creating appropriate index types (e.g., single-column, composite, unique), and regularly analyzing index usage and effectiveness.
- **Query Optimization**
  - Query optimization is the process of selecting the most efficient way to execute a SQL query. It involves the database management system (DBMS) analyzing different possible execution plans for a query and choosing the one that will return the results fastest, using the least amount of resources.
- **Transaction Isolation Levels**
  - Transaction isolation levels in SQL define the degree to which the operations in one transaction are visible to other concurrent transactions. There are typically four standard levels: Read Uncommitted, Read Committed, Repeatable Read, and Serializable.

---

## 3. Advanced

### 3.1 Transactions
- **BEGIN**
  - BEGIN is used in SQL to start a transaction, which is a sequence of one or more SQL operations that are executed as a single unit. A transaction ensures that all operations within it are completed successfully before any changes are committed to the database.
- **COMMIT**
  - COMMIT is an SQL command that saves all changes made during a transaction to the database. Until a COMMIT command is issued, all modifications within a transaction are only temporary and visible to the current session.
- **ROLLBACK**
  - ROLLBACK is a SQL command used to undo transactions that have not yet been committed to the database. It reverses all changes made within the current transaction, restoring the database to its state before the transaction began.
- **SAVEPOINT**
  - A SAVEPOINT in SQL is a point within a transaction that can be referenced later. It allows for more granular control over transactions by creating intermediate points to which you can roll back without affecting the entire transaction.
- **ACID**
  - ACID are the four properties of relational database systems that help in making sure that we are able to perform the transactions in a reliable manner. It's an acronym which refers to the presence of four properties: atomicity, consistency, isolation and durability
- **rank**
  - The RANK function in SQL is a window function that assigns a rank to each row within a partition of a result set, based on the order specified by the ORDER BY clause. Unlike the ROWNUMBER function, RANK allows for the possibility of ties—rows with equal values in the ordering column(s) receive the same rank, and the next rank is skipped accordingly.
- **dense_rank**
  - denserank is a window function that assigns a rank to each row within a partition of a result set, based on the order of rows. Unlike the rank function, denserank assigns consecutive ranks without gaps, even when there are ties in the ordering criteria.
- **lead**
  - LEAD is a window function in SQL that provides access to a row at a specified offset after the current row within a partition. It's the counterpart to the LAG function, allowing you to look ahead in your dataset rather than behind.
- **lag**
  - LAG is a window function in SQL that provides access to a row at a specified offset prior to the current row within a partition. It allows you to compare the current row's values with previous rows' values without using self-joins.

### 3.2 Data Integrity & Security
- **Data Integrity Constraints**
  - Data integrity constraints are rules you set up in a database to make sure the data is accurate and reliable. These rules prevent bad data from being entered into tables.
- **GRANT and Revoke**
  - GRANT and REVOKE are SQL commands used to manage user permissions in a database. GRANT is used to give specific privileges (such as SELECT, INSERT, UPDATE, DELETE) on database objects to users or roles, while REVOKE is used to remove these privileges.
- **DB Security Best Practices**
  - Database security best practices are a collection of methods used to protect sensitive data from unauthorized access, modification, or deletion. They involve implementing access controls based on the least privilege principle, routinely updating systems, using strong passwords, limiting remote access, avoiding the admin account for everyday tasks, encrypting communication, performing regular backups, monitoring and auditing database operations, performing vulnerability scanning, and guarding against SQL injection attacks by using parameterized queries or prepared statements.

### 3.3 Stored Procedures & Functions
- **DATEPART**
  - DATEPART is a useful function in SQL that allows you to extract a specific part of a date or time field. You can use it to get the year, quarter, month, day of the year, day, week, weekday, hour, minute, second, or millisecond from any date or time expression.

### 3.4 Performance Optimization
- **Using Indexes**
  - Indexes in SQL are database objects that improve the speed of data retrieval operations on database tables. They work similarly to an index in a book, allowing the database engine to quickly locate data without scanning the entire table.
- **Optimizing Joins**
  - Optimizing joins in SQL involves techniques to improve the performance of queries that combine data from multiple tables. Key strategies include using appropriate join types (e.g., INNER JOIN for matching rows only, LEFT JOIN for all rows from one table), indexing the columns used in join conditions to speed up lookups, and minimizing the data processed by filtering results with WHERE clauses before the join.
- **Query Analysis Techniques**
  - Understanding how SQL queries are executed is essential for performance tuning. Tools like EXPLAIN or EXPLAIN PLAN allow you to dissect the execution plan the database uses for a specific query.

### 3.5 Advanced SQL
- **Reducing Subqueries**
  - Reducing subqueries is a common SQL optimization technique, especially when dealing with complex logic or large datasets. Correlated subqueries, which are evaluated once for each row in the outer query, can degrade the performance.
- **Selective Projection**
  - Selective projection in SQL refers to the practice of choosing only specific columns (attributes) from a table or query result, rather than selecting all available columns. This technique is crucial for optimizing query performance and reducing unnecessary data transfer.
- **Recursive Queries**
  - Recursive queries are SQL queries that refer to themselves within their own definition. They're used to process hierarchical or tree-structured data, where relationships exist between rows in the same table, like organizational charts, bill of materials, or social networks.
- **Pivot / Unpivot Operations**
  - Pivot and unpivot operations transform the structure of data within a table. Pivoting rotates rows into columns, aggregating data based on common values.
- **Window Functions**
  - Window functions perform calculations across a set of rows that are related to the current row. Unlike standard aggregate functions that group rows into a single result row, window functions retain the individual rows and add a calculated value for each row based on the window frame.
- **Common Table Expressions**
  - Common Table Expressions (CTEs) in SQL are named temporary result sets that exist within the scope of a single SELECT, INSERT, UPDATE, DELETE, or MERGE statement. Defined using the WITH clause, CTEs act like virtual tables that can be referenced multiple times within a query.
- **Dynamic SQL**
  - Dynamic SQL refers to the ability to construct and execute SQL statements programmatically during runtime. Instead of writing static SQL queries directly into your code, you can build SQL strings based on varying conditions, user inputs, or other dynamic factors.
- **row_number**
  - ROW\NUMBER() is a SQL window function that assigns a unique, sequential integer to each row within a partition of a result set. It's useful for creating row identifiers, implementing pagination, or finding the nth highest/lowest value in a group.
- **first_value**
  - Understand fundamental concepts, architectures, and implementation practices of first_value.

---

## 4. Optional / Specialized Topics

- INSERT
- UPDATE
- DELETE
- MIN
- MAX
- HAVING
- Primary Key
- Foreign Key
- Unique
- NOT NULL
- CHECK
- FLOOR
- ABS
- MOD
- ROUND
- CEILING
- Nested Subqueries
- Correlated Subqueries
- DATE
- TIME
- TIMESTAMP
- DATEADD
- Creating Views
- Modifying Views
- Dropping Views

---

## 5. References

- [SQL Roadmap](https://roadmap.sh/sql)

---

## 6. Related Roles / Topics

### Related Roles
- PostgreSQL DBA
- Backend Developer
- DevOps Engineer

### Related Skills
- C++