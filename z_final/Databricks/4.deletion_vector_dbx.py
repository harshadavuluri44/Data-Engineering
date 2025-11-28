"""
What happens when you DELETE or UPDATE a row in Delta Lake?

---------------------------------------------------------------------------------------------------

Traditional Method:
    
    Assume there are 100 rows in xyz.parquet, referenced by the Delta log and Delta table.

If we delete 15 rows:
    Delta Lake does NOT modify the original parquet file in place.
    Instead, it writes a new parquet file with the remaining rows.
    The Delta transaction log (_delta_log/) is updated to:
        Mark the old file as removed (not physically deleted immediately).
        Add a reference to the new file.

    Eventually, VACUUM removes the old parquet file (xyz.parquet) once it is no longer referenced.

-----------------------------------------------------------------------------------------------

Latest Method: Deletion Vectors (DVs) in Databricks Delta Lake
    
    A Deletion Vector is a mechanism to logically delete rows without rewriting the underlying data
    file.
    Instead of creating new parquet files during DELETE/UPDATE, Delta marks rows as "deleted" 
    using DVs.

Why are Deletion Vectors needed?
    Rewriting entire parquet files for every DELETE/UPDATE is expensive for large datasets.
    DVs avoid costly rewrites by tracking deleted rows separately.

------------------------------------------------------------------------------------------------

What is a Deletion Vector?
    
    A Deletion Vector is a compact bitmap or list that marks which rows in a data file are deleted.
    It is stored alongside the data file and referenced in the Delta table's metadata.
    On read, Delta Lake automatically skips rows marked as deleted.
    Implementation details:
        * DV information is stored in a small .bin file within the _delta_log folder.
        * The Delta transaction log JSON files reference these DVs.

--------------------------------------------------------------------------------------------------

Important Notes:

VACUUM:
    Does NOT delete rows inside parquet files if other rows are still alive.
    Only deletes entire parquet files if they are completely unreferenced in the Delta log.

OPTIMIZE:
    Creates a new compacted parquet file containing only alive rows.
    The old parquet file becomes unreferenced by the Delta log and is eventually removed by VACUUM.
    This resembles the traditional method but does not occur on every DELETE/UPDATE.

--------------------------------------------------------------------------------------------------

Summary:
    Traditional Method → Rewrite parquet files + update Delta log + VACUUM removes old files.
    Deletion Vectors → Logically delete rows (no file rewrite) using compact metadata.
    OPTIMIZE + VACUUM → Physically remove unreferenced files when needed.

"""
