'''

what is metadata optimization in Databricks / Delta Lake?

-------------------------------------------------------------------------------------------

When we store huge Delta tables (hundreds of GBs to multi-TB), then number of files and file
level information grows very fast.

Spark must read this metadata before scanning the actual data.

Metadata examples:

    List of files in each partition
    Schema information
    Min/Max values statistics per file
    Partition layout
    Delta logs (_delta_log JSON files)


As the table grows, this metadata becomes large, and Spark spends time scanning that before it
even touches real data.


Techniques for Metadata Optimization

OPTIMIZE command (file compaction + ZORDER)
VACUUM (Deletes old data files and delta logs JSON files that are no longer needed)

'''