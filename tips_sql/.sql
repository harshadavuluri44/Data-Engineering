-- The AS keyword creates a temporary column alias for a column

-- NOT EQUAL TO :-  <>

SELECT *, Name as CountryNAME FROM world.Country LIMIT 10;


SELECT * FROM table WHERE name LIKE 'Jhon%';
SELECT * FROM table WHERE name LIKE '%aa%';


SELECT * FROM table WHERE name IN ('fata','derek','jeff');

-- BETWEEN :- range is inclsuive
SELECT * FROM table WHERE amount BETWEEN 100 and 200;

-- IS NULL :- returns rows which are null
-- IS NOT NULL :- returns rows which are not null (doesnt return or check empty values)
SELECT * FROM table WHERE name IS NULL;
SELECT * FROM table WHERE name IS NOT NULL;

SELECT * FROM table WHERE name='fata' AND age='44';
SELECT * FROM table WHERE name='fata' OR age='44'


-- SUM,COUNT,AVG,MIN and MAX works on specific column

SELECT COUNT(col_name) FROM table; SELECT COUNT(*) FROM table; -- Both are same
SELECT COUNT(DISTINCT col_name) FROM table:

SELECT Country, COUNT(*) as count FROM table GROUP BY CountryCode;
SELECT Country, District, COUNT(*) as count FROM table GROUP BY CountryCode, District;

-- ORDER OF EXECUTION
-- FROM -> JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

SELECT year, month, MAX(stock_high) as stock_high
FROM table GROUP BY year, month HAVING stock_high > 1000 AND ORDER BY stock_high DESC;

-- DISTINCT gets applied for both columns
SELECT DISTINCT year, month FROM apple_stocks;


-- ORDER of writing code :- INNER JOIN -> WHERE

-- FROM -> JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
   -- WHEN HAVING RUNS, the alias FROM SELECT hasn't been computed yet
   -- So we must use full aggregate expression in HAVING

-- NOTE :- CTE returns temporary table with atleast 1 column and 1 row but not a scalar value

-- IN (1,2,3,5)  ,  SELECT * FROM table WHERE col_1 IN (SELECT col_2 FROM table_name)

----------------------------------

DIFF BETWEEN INNER JOIN, LEFT JOIN, RIGHT JOIN

INNER JOIN returns only matching rows from both tables based on codition
LEFT JOIN returns all rows from left table and matching rows from right table
RIGHT JOIN returns all rows from right table and matching rows from left table

A-> a,  B-> B

be careful while selecting values

SELECT a.col1, a.col2, b.col1, b.col2 vs SELECT a.col1, a.col2, a.col3, b.col2

MATHCING COLUMN b.col1=a.col3

--------------------------------------------------

PRIMARY KEY in sql table is a column (or a combination of columns) that uniquely indentifies each
row in a table

Key characteristics:
* Unique - No two rows can have same primary key value
* Not Null - Primary key values cannot be NULL
* One per Table - A table can have only one primary key
* Used for Relationships - Often referenced by foreign keys in other tables.

Composite Primary Key :- If uniqueness depends on combination of columns:

Example :- CREATE TABLE enrollments (
               student_id INT, course_id INT, name STRING,
               PRIMARY KEY (student_id, course_id)
);

--------------------------------------------------------------------------------------

IMPORTANT -> WHERE id = NULL (wrong)  id IS NULL (True)

--------------------------------------------------------------------------------------

ON w.date = x.date + INTERVAL 1 DAY

---------------------------------------------------

bonus <1000 doesn't return NULL's
INSTEAD bonus <1000 or bonus IS NULL

----------------------------------------------

syntax for two temp_table 's in SQL query


WITH temp_table_1 AS (

),
temp_table_2 AS (

)

but dont use WITH twice ....
------------------------------------------------------------------------------------------------

SELECT * FROM table WHERE col_a=col_b=col_c (WRONG)

SELECT * FROM table WHERE col_a=col_b AND col_b=col_c

------------------------------------------------------------------------------------------------

DELETE FROM table_name WHERE -> valid
DELETE * FROM table_name WHERE  -> * is invalid
----------------------------------------------------------------------------------------------------

In many cases, instead of creating a temp table or writing a CTE just to filter results of window 
function, we can directly use QUALIFY

without QUALIFY (using CTE)

with ranked AS (
      SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
      FROM employees
)
SELECT * FROM ranked WHERE rn = 1;

with QUALIFY (simpler)

SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
      FROM employees
      QUALIFY rn=1;

-------------------------------------------------------------------------------------------------