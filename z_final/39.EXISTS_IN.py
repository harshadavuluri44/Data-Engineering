'''

IN operator is used in WHERE clause to check if column value matches any value in list or result 
set from a subquery


-> It's like writing multiple OR conditions in a shorter and cleaner way


SELECT * FROM employees
WHERE department IN ('HR', 'Finance', 'IT');

==

SELECT * FROM employees
WHERE department = 'HR'
   OR department = 'Finance'
   OR department = 'IT';


Using IN with subquery

SELECT * FROM employees
WHERE department_id IN (
    SELECT department_id FROM departments
    WHERE location = 'NY'
);


IN  **  NOT IN

------------------------------------------------------------------------------------------------

EXISTS check whether atleast one row is return by subquery or not


'''