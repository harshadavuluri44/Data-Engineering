-- The AS keyword creates a temporary column alias for a column

-- NOT EQUAL TO :-  <>



-- BETWEEN :- range is inclsuive
SELECT * FROM table WHERE amount BETWEEN 100 and 200;

-- DISTINCT gets applied for both columns
SELECT DISTINCT year, month FROM apple_stocks;


-- FROM -> JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
   -- WHEN HAVING RUNS, the alias FROM SELECT hasn't been computed yet
   -- So we must use full aggregate expression in HAVING

-----------------------------------------------------------------------------------------------

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

ON w.date = x.date + INTERVAL 1 DAY

------------------------------------------------------------------------------------------------

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