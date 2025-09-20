'''
How do you handle data integration from multiple sources?

1. Identiy and connect to sources
    * Could be databases (MySQL, Postgres), APIs, files(CSV, JSON, Parquet), Streaming Systems(kafka)
    * Read whole data using connectors in PySpark/ Databricks:
        -> spark.read.format('jdbc') for database
        -> spark.read.format('json/parquet') for files
        -> Structured streaming for kafka/Event hubs

2. Ingest data into a single landing/ storage zone
    * store raw data in a centralized location (data lake)
    * Examples : AWS S3, Azure Data Lake, GCP cloud storage

3. Normalize and Standardize
    * Different sources may have: Different schemas (column names, data types)
    * Transform to a common schema using pyspark:
        -> Rename columns, convert data types, Handle nulls/missing fields

4. Merge/ join datasets
    * Use joins, unions, or MERGE to combine data into integrated tables

5. Load into target tables

6. Automate & Schedule
'''