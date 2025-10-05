"""
SQL Join Types in Spark / SQL

FULL JOIN / FULL OUTER JOIN
    Combination of LEFT JOIN and RIGHT JOIN.
    Returns all records from both left and right tables.
    If the ON condition matches, values from both tables are shown.
    If there is no match, unmatched columns are filled with NULL.
    Example:
        SELECT A.id, A.name, B.city
        FROM A
        FULL OUTER JOIN B
        ON A.id = B.id

------------------------------------------------------------------------------------------------

CROSS JOIN / CARTESIAN JOIN
    Returns the Cartesian product of two tables.
    Every row from the first table is combined with every row from the second table.
    No ON condition is used.
    Syntax:
        SELECT A.id, A.name, B.city
        FROM A
        CROSS JOIN B
    Number of rows in result = (rows in A) * (rows in B)

--------------------------------------------------------------------------------------------------

LEFT ANTI JOIN
    Returns rows from the left table that do not match any row in the right table based on the ON 
    condition.
    Example:
        SELECT A.*
        FROM A
        LEFT ANTI JOIN B
        ON A.id = B.id

        
"""
