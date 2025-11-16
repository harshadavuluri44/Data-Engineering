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

NOTE :- OPTIMIZE does not change how the data is ordered inside the files unless we explicitly
use ZORDER

--------------------------------------------------------------------------------------------------

ZORDER

A multi-dimensional clustering technique that arranges related data across multiple columns so
they sit close together in the same files.

After Delta Lake compacts small files into larger ones using OPTIMIZE, Z-ORDER reorganizes 
the rows inside those files so that similar values (across chosen columns) are placed near 
each other on disk.

OPTIMIZE sales
ZORDER BY (customer_id, product_id);

------------------------------------------------------------------------------------------

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


2. OPTIMIZE my_table ZORDER By (col1, col2);

After compaction,

For each row, Delta computes a  Z-value, later Z-order curve.

Rows are sorted by this Z-value.

Rows with similar values end up stored physically close together inside the file.


'''