'''

WHAT IS A DATA LAKEHOUSE?

A Data Lakehouse is a centralized data platform that combines the flexibility and scalability of a 
data lake with the structured data management, reliability, and high-performance query capabilities 
of a data warehouse. It allows organizations to store all types of data—structured, semi-structured,
and unstructured.

------------------------------------------------------------------------------------------

WHY LAKEHOUSE ?

Data lakes -> stores everything,        but messy, slow queries, hard governance.
Data warehouses -> clean, fast queries, but expensive and rigid


A LAKEHOUSE solve this by layering warehouse-like features (schema, ACID transactions, governance,
performance optimizations) on top of a data lake storage (S3, ADLS, GCS)

-------------------------------------------------------------------------------------------------

CORE COMPONENTS OF DATA LAKEHOUSE ARCHITECTURE

1. DATA SOURCE LAYER : Structured (OLTP db's, ERP, CRM)
                       Semi-structured (JSON, logs)
                       Unstructured (images, videos, text)

2. INGESTION LAYER : Brings data from sources through batch + streaming modes (kafka, kinesis, dbx)

3. STORAGE LAYER : object storage (S3, ADLS, GCS)

     But data is stored in optimized table formats like Delta Lake,
                                                        Apache Iceberg,
                                                        Apache Hudi

    These formats add:
        -> Schema enforcement
        -> ACID transactions
        -> Versioning (time travel)
        -> Indexing / caching for faster queries

    This is what upgrades a plain data lake into delta lake (a lakehouse)

4. PROCESSING & ANALYTICS LAYER : This is where data is cleaned, transformed and prepared.

    Apply ETL or ELT here depending on the use case.

    Tools : Databricks (Delta Lake), Spark

5. GOVERNANCE & SECURITY LAYER (very strong in lakehouse)

    Unified catalog (e.g., Databricks Unity Catalog, AWS Glue catalogs)

6. CONSUMPTION/ PRESENTATION LAYER :
   
    BI, SQL queries (Databricks SQL, Athena)
    Data Science/ML (SageMaker, MLFlow, Databricks ML)


EXAMPLES OF LAKEHOUSE PLATFORMS

Databricks Lakehouse (Delta Lake + Unity Catalog)



'''