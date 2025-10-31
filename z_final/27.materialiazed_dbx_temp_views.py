"""

Materialized View (MV):

  A MV is like a pre-computed table that stores the actual physical data on disk.
  Created using a SQL query (SELECT ...) just like a normal view.
  Instead of executing the query every time, the system stores the results.
  Often refreshed periodically (e.g., every hour/day) or manually to keep up with changes in base 
  tables.

Purpose: Performance optimization, especially for complex joins/aggregations in large data warehouses.


Example:

    CREATE MATERIALIZED VIEW mv_sales_summary AS
    SELECT region, product, SUM(sales) AS total_sales 
    FROM sales_table
    GROUP BY region, product;

------------------------------------------------------------------------------------------------

DBX View (Databricks View):

  A logical object stored in Hive Metastore / Unity Catalog.
  Does NOT store data physically.
  Every time we query the view, Databricks re-runs the underlying SQL on the base tables.


Example:
    CREATE VIEW mv_sales_summary AS
    SELECT region, product, SUM(sales) AS total_sales 
    FROM sales_table
    GROUP BY region, product;

-----------------------------------------------------------------------------------------------

Spark Temporary View:

  Created using df.createOrReplaceTempView('temp_view_name').

  In-memory view valid only within the current Spark session/notebook.
  Stored in Spark Session Catalog (not in Hive or Unity Catalog).
  Once the cluster is restarted or session ends, it disappears.
  Does NOT store data; just an alias for a DataFrame query plan.

----------------------------------------------------------------------------------------------

Key Differences:

Feature                | Materialized View (MV) | DBX View              | Spark Temp View
---------------------  | ---------------------  | -----------------     | ----------------
Data Stored?           | Yes (on disk)          | No                    | No
Performance Benefit    | Faster                 | Depends on base table | Depends on base table
Refresh Needed?        | Yes                    | No                    | No

-------------------------------------------------------------------------------------------------

Summary:
  Use MV when you need a performance boost by avoiding recomputation of heavy queries.
  Use DBX View when you want reusable, maintainable SQL logic over base tables.
  Use Spark Temp View when quickly querying a DataFrame in your current notebook/session.


"""
