WITH t1 AS (
    SELECT emp_name, salary, ROW_NUMBER() OVER(ORDER BY salary) as rn,
    COUNT(*) OVER() as total_employees FROM employee_table
)

SELECT AVG(salary) as median_salary
FROM t1
WHERE rn = (total_employees + 1)/2 or rn = (total_employees + 2)/2



-- When we need value, add it is column to table and use it