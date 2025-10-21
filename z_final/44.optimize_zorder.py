'''

What are OPTIMIZE and ZORDER?

Both are performance optimization commands for Delta table in Databricks

They help make queries faster and more efficient, especially on large datasets

---------------------------------------------------------------------------------------

Why do we need OPTIMIZE ?

When Delta tables are updated or appended frequently, many small parquet files get created in table's
storage location.

These small files cause:
    slow query performance

    

OPTIMIZE fixes this by compacting many small parquet files into a few large files.

--------------------------------------------------------------------------------------------------

ZORDER - Cluster Data for faster filtering

After compacting files with OPTIMZIE, we can organize data inside those files, using Z-ordering - a
smart way of clustering related data together


ZORDER BY (column_name) rearranges data so that rows with similar values are stored close together
on disk.


'''