'''
Materialized View (MV) :- A MV is like a pre-computed table that stores the actual physical data on
disk.

* It is created using SQL query (SELECT ...) just like a normal view - but instead of executing query
  every time, the system stores the results.

* They are often refreshed periodically (e.g, every hour/day) or manually, to keep up with changes in
  the changes in base tables.

* Purpose: Performance optimization, especially for complex joins/aggregations in large DW's.

Example :

CREATE MATERIALIZED VIEW mv_sales_summary AS
SELECT region, product, SUM(sales) AS total_sales FROM sales_table
GROUP BY region, product;
------------------------------------------------------------------------------------------------

DBX view is a logical object stored in Hive Metastore / unity catalog.

* It does NOT store data physically.

* Every time we query view, DBX will re-run the underlying SQL on base tables.

CREATE VIEW mv_sales_summary AS
SELECT region, product, SUM(sales) AS total_sales FROM sales_table
GROUP BY region, product;
--------------------------------------------------------------------------------------------------

Spark Temporary View (df.createOrReplaceTempView('temp_view_name'))

This is an in-memory view valid only within the current Spark session/ notebook.

* Stored in Spark Session Catalog (not in Hive or unity)

* Once cluster is restarted or session ends - it disappears

* Also does NOT store data - just an alias for a DF query plan
----------------------------------------------------------------------------------------------------

Key Differences         

Feature                 MV               DBX view              Spark Temp view

Data Stored?            yes (on disk)    No                    No

Performance Benefit     Faster           Depends on base table Depends on base table

Refresh Needed?         yes              No                    No 
-------------------------------------------------------------------------------------------------

SUMMARY

Use MV when we need performance boost by avoding recomputation of heavy queries

Use DBX views when you want reusable, maintainable SQL logic over base tables

use temp_view when quickly querying a DF in your current notebook/ session
'''