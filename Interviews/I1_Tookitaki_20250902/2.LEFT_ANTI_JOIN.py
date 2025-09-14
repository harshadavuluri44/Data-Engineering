'''

LEFT JOIN (also called LEFT OUTER JOIN) returns all rows from left table, and the matching rows 
from right table. 

If no match is found -> the left row still appears, but right side columns are filled with NULLS

-----------------------------------------------------------------------------------------

LEFT ANTI JOIN returns rows from left table that do not have a match in right table on join 
column.

LEFT ANTI JOIN is opposite of LEFT JOIN


EXAMPLE :- Select all customers who never placed an order

SELECT c.customers FROM customers c
LEFT ANTI JOIN orders o 
ON c.customer_id = o.customer_id

'''