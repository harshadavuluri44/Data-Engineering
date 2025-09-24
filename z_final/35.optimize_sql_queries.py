'''

1.  Optimize SELECT statements

    Select only required columns - Avoid select *
    Filter early - Use WHERE clauses to limit rows as early as possible

2.  Use Indexing 

    Create indexes on frequently searched columns : Primary keys, foreign keys, and columns in WHERE,
    JOIN, and ORDER BY.

    Use composite indexes carefully: For queries filtering on multiple columns

    Avoid over-indexing: Too many indexes can slow down INSERT, UPDATE, and DELETE

3. Optimize Joins

    Join order matters : start with smaller tables or highly filtered data
    
    Use appropriate join types : For example, avoid CROSS JOIN unlessnecessary

    Consider EXISTS instead of IN : EXISTS can be faster on large datasets

4. Optimize Aggregations

Use indexed columns for GROUP BY and ORDER BY.

Pre-aggregate if possible: Use summary tables for frequent heavy aggregation.

5. Reduce Subqueries

Use JOINs instead of correlated subqueries where possible.

-- Slow
SELECT name FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id)

-- Faster
SELECT DISTINCT c.name
FROM customers c
JOIN orders o ON o.customer_id = c.id

6. Limit Data

Use LIMIT / TOP if only a subset is needed.

Partition large tables: Query only relevant partitions.

7. Analyze Execution Plans

Use EXPLAIN (MySQL, PostgreSQL) or EXPLAIN PLAN (Oracle) to see how SQL engine executes queries.

Identify table scans, missing indexes, and costly operations.

8. Optimize Updates & Deletes

Batch operations: Avoid updating/deleting millions of rows in a single query.

Filter precisely: Use indexed columns in WHERE.

9. Consider Caching & Materialized Views

Materialized views: Precompute heavy joins or aggregations.

Query caching: Some DBs cache query results for faster retrieval.

10. Database-Specific Optimizations

Partitioning: Horizontal or vertical partitioning of large tables.

Proper data types: Smaller, appropriate data types reduce I/O.

Use hints (if needed): In databases like Oracle, you can give the optimizer hints for joins or indexes.
'''