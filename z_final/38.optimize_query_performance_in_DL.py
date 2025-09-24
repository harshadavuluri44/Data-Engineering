'''

How would you optimize query performance in a Data Lake?

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
'''