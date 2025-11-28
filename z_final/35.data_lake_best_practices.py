'''

Data Lake Query Optimization
---------------------------------------------------------------------------------------------

Use columnar file formats

    Store data in Parquet, ORC or Avro to reduce I/O by reading only required columns.

Partitioning

    Organize data into folders based on frequently queried fields, so queries scan only relevant
    partitions

Data Pruning & filtering

    Apply filters early in queries to minimize the data scanned

File sizing & compaction

    Avoid too many small files: compact them to reduce overhead

Metadata Management 

    Maintain up-to-date metadata in data catalog so engines can efficiently locate files and infer
    schema


Pre aggregation / materialized views 

    Store frequently computed aggregates to reduce rutime computation


---------------------------------------------------------------------------------------------

Partitioning Best Practices


Partitioning is critical in a Data Lake because it affects query performance, cost, and scalability.


1. Choose the Right Partition column(s)

    Use low-to-medium cardinality columns for partitioning, avoid high-cardinality columns because
    it can create too many small files

2. Do multi-level partitioning helps prune data efficiently

3. Ensure sql queries filter on partition columns, this allows spark to skip unnecessary files,
   drastically improving performance

4. Do partitioning, file size optimization, and metadata management using OPTIMIZE + ZORDER

5. seperate hot data vs cold data

    Push frequently resused data (hot cold) into separate partitions

'''