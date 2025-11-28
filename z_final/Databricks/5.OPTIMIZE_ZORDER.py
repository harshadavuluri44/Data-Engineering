'''

What are OPTIMIZE and ZORDER?

Optimize and Zorder are delta lake features only available on Databricks.

------------------------------------------------------------------------------------------------------

Both are performance optimization commands for Delta table in Databricks

They help make queries faster and more efficient, especially on large datasets

------------------------------------------------------------------------------------------------------

Why do we need OPTIMIZE ?

When Delta tables are updated or appended frequently, many small parquet files get created in table's
storage location.

These small files cause:
    slow query performance

    

OPTIMIZE fixes this by compacting many small parquet files into a few large files.

NOTE :- OPTIMIZE does not change how the data is ordered inside the files unless we explicitly
use ZORDER

------------------------------------------------------------------------------------------------------

Z-Ordering

A multi-dimensional data clustering technique in Databricks Delta Lake that arranges related data across
multiple columns to sit close together in the same set of files.

After Delta Lake compacts small files into larger ones using OPTIMIZE, Z-ORDER reorganizes the rows 
inside those files so that similar values (across chosen columns) are placed near each other on disk.

OPTIMIZE sales
ZORDER BY (customer_id, product_id);


* APPLY Z-order on frequently queried columns

AVoid Z-order when 
        table is small (little benfit)
        we don't filter frequently on column
        if table is frequently updated/deleted (reordering is expensive)


How Z Order works?

After compaction by OPTIMIZE

    i) For each row, Delta computes a  Z-value, later Z-order curve.
    ii)Rows are sorted by this Z-value.
    iii)Rows with similar values end up stored physically close together inside the file.

------------------------------------------------------------------------------------------------------

LIQUID CLUSTERING

A dynamic, self-optimizing clustering method in Delta Lake (Databricks).

Automatically reorganizes data for optimal query performance 
Reduces need for manual OPTIMIZE ... ZORDER BY

-----------------------------------------------------------------------------------------

VACUUM

VACUUM deletes only physcial files in table's storage location that are no longer referenced
in Delta LOG and older than the RETAIN period

NOTE :- It does NOT delete data from table.

-------------------------------------------------------------------------------------------

How OPTIMIZE and ZORDER works Internally ?


1. Compaction  OPTIMIZE my_table;


Spark scans metadata to identify small files in each partition

Spark read those files in parallel. (i.e writes them into worker nodes storage)

Combines them into new, large Parquet files (typically 1GB)

Writes new files back to storage

Mark old files as remove in _delta_log, but doesn't delete (VACUUM does that)



'''