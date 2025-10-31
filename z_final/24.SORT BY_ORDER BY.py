'''
IN SQL, ORDER BY

    Performs a global ordering of the result set.
    Guarantees that the entire output is sorted across all partitions.


EXAMPLE:
SELECT * FROM customers
ORDER BY age DESC;

-----------------------------------------------------------------------------------------------

IN SQL, SORT BY

    Performs a local ordering within each partition of data.
    Does NOT guarantee global ordering across partitions.


EXAMPLE:
SELECT * FROM customers
SORT BY age DESC;

--------------------------------------------------------------------------------------------------

ORDER BY is more expensive, since it requires full shuffle of all data
wherease
SORT BY is cheaper than ORDER BY, because it avoids full shuffle (just shuffle across partitions)

'''
