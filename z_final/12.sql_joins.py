'''
FULL JOIN / FULL OUTER JOIN (combination of left join and right join)

Gives records from left table and right table also
if matches with ON condition values are shown in results
else values will be null
-------------------------------------------------------------------------

CROSS JOIN / CARTESIAN JOIN

It returns cartesian product of two tables - meaning every row from first table is combined with 
every row from second table

SYNTAX :- SELECT A.id, A.name, B.city
          FROM A
          CROSS JOIN B

Number of rows in result = (rows in A) * (rows in B)

* No ON condition is used
--------------------------------------------------------------------------------

LEFT ANTI JOIN

Gives rows from left table which dont match with ON condition
'''