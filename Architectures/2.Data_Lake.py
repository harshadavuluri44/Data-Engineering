'''

WHAT IS DATA LAKE ?

A Data Lake is a centralized repository that stores all kinds of data - structured, semi-structured,
and unstructured - in its raw/native format until it's needed. Unlike a warehouse, it doesn't
enforce schema-on-write; instead, it uses schema-on-read.

---------------------------------------------------------------------------------------------

KEY LAYERS OF DATA LAKE ARCHITECTURE

1. DATA SOURCE LAYER : Structured (databases, OLTP, ERP, CRM)
                       Semi-structured (JSON, CSV, XML)
                       Unstructured (images, videos, PDFs)
                       Streaming data (kafka, Kinesis, EventHub)

                       
2. INGESTION LAYER : Brings data from above various sources into Data lake in batch or streaming mode

3. STORAGE LAYER : The actual data lake, where our data resides. Typically organized in original
   format.

   AWS S3, Azure Data Lake Storage (ADLS), Google Cloud Storage (GCS),
   HDFS (on-premises)

Streaming logs from website -> Amazon Kinesis -> Data Lake

4. PROCESSING/ ANALYTICS LAYER : This is where data is cleaned, transformed and prepared.

    Apply ETL or ELT here depending on the use case.

    Tools/Engines :- Spark, Databricks etc

5. CONSUMPTION/ PRESENTATION LAYER : Data is queried and consumed directly from lake or after
   curation.

   Tools : Databricks ML, sagemaker

6. Governance & Security Layer : Manages access control, cataloging, lineage, and compliance

    Ex :- Databricks Unity Catalog


    
DATA LAKE EXAMPLE 

 Source data lands in s3 ->

 ETL/ ELT Processing ->

 Store as Databricks Tables (s3 storage location)

'''