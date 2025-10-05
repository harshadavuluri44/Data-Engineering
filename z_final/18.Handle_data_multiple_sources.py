"""
How do you handle data integration from multiple sources?

----------------------------------------------------------------------------------------------

1. Identify and Connect to Sources
    
    Sources can include:
        Databases (MySQL, PostgreSQL, Oracle, SQL Server)
        APIs
        Files (CSV, JSON, Parquet, Avro, etc.)
        Streaming Systems (Kafka, Event Hubs)
    
    Read data using connectors in PySpark/Databricks:
        -> spark.read.format('jdbc') for databases
        -> spark.read.format('json') or spark.read.format('parquet') for files
        -> Structured Streaming for Kafka/Event Hubs

----------------------------------------------------------------------------------------------

2. Ingest Data into a Centralized Landing Zone
    
    Store raw data in a centralized location (data lake / staging area).

Examples: AWS S3, Azure Data Lake Storage (ADLS), GCP Cloud Storage.

-----------------------------------------------------------------------------------------------

3. Normalize and Standardize
    
    Different sources may have different schemas (column names, data types).
    Transform into a common schema using PySpark:
        Rename columns
        Convert data types
        Handle nulls/missing fields
        Standardize formats (e.g., date/time, currency)

-----------------------------------------------------------------------------------------------

4. Merge / Join Datasets
    
    Use joins, unions, or MERGE operations to combine data into integrated tables.
    Ensure primary keys / unique IDs are handled correctly.

------------------------------------------------------------------------------------------------

5. Load into Target Tables
    
    Store integrated, cleaned data in curated tables (Data Warehouse / Delta Lake).
    
Examples: Redshift, BigQuery, Snowflake, Databricks Delta Tables.

------------------------------------------------------------------------------------------------

6. Automate & Schedule
    
    Automate workflows using orchestration tools:
        Airflow, Databricks Workflows, Azure Data Factory, AWS Glue.
    
    Schedule jobs to run periodically or trigger-based (batch or streaming).

------------------------------------------------------------------------------------------------

Summary: Connect to multiple sources → Ingest → Standardize → Integrate → Load → Automate.

"""
