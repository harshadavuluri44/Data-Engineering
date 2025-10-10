'''
IN SQL, ORDER BY

    Performs a global ordering of the result set.
    Guarantees that the entire output is sorted across all partitions.
    More expensive, since it requires a full shuffle of all data.

EXAMPLE:
SELECT * FROM customers
ORDER BY age DESC;

-----------------------------------------------------------------------------------------------

IN SQL, SORT BY

    Performs a local ordering within each partition of data.
    Does NOT guarantee global ordering across partitions.
    Cheaper than ORDER BY, because it avoids a full shuffle.

EXAMPLE:
SELECT * FROM customers
SORT BY age DESC;


'''
