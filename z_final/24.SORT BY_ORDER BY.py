'''

In SQL, ORDER BY

* Performs a global ordering of the result set.
* Guarantees that entire output is sorted across all partitions
* More expensive, since it requires a full shuffle of all data

SELECT * FROM customers
ORDER BY age DESC;

'''

'''

IN SQL, SORT BY

* Performs a local ordering within each partition of data.
* Does not guarantee global ordering across all partitions.
* Cheaper than ORDER BY, because it avoids a full shuffle.

SELECT * FROM customers
SORT BY age DESC;

'''