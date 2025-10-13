'''

AWS Glue

1. Managed Extract, Transform, and load (ETL) service

2. Fully serverless service


the word 'managed' means that AWS takes care of infrastructure, scaling, maintenance and availability
for us.

        s3 Bucket
                    ->    Extract  ->  (Glue ETL - Transform) - >  Load  ->  Redshift Data Warehouse
        Amazon RDS

----------------------------------------------------------------------------------------------------

AWS Glue has 2 main features :- Data Catalog and Spark ETL engine

DATA CATALOG stores metadata of Data Sources (data stored in S3, RDS etc), i.e schema, data location

------------------------------------------------------------------------------------------------

AWS Glue DATA CATALOG components


CRAWLERS :- Crawler is a program that connects to the data source and automatically scans data in data
sources to determine its metadata, schema and create metadata tables in the AWS Glue Data Catalog


        DATA SOURCE   -    CRAWLER    -    DATA CATALOG


We might get a thought that source might be same always and we recieve data under that, So crawler
need not be scheduled. 

But we may have partitions under source folder, those to be registered in data catalog for Athena and
Glue ETL

Crawler should be scheduled to track schema evolution changes

Manuall crawler creation in AWS needs Database name to create tables to store metadata of source data
and source data location. That's it.

------------------------------------------------------------------------------------------------------


IMPORTANT POINT

Now we can go to AWS Athena console and give Data Source of AWSGlueDatCatalog , select Database and
run sql query to see the data

So The metadata we stored in AWSGlueDataCatalog Tables is used by sql query

---------------------------------------------------------------------------------------------------

CONNECTIONS 

ETL jobs needs to load data from source location - So we store the 

1. choose source locations (s3/ Aurora DB/ JDBC, etc)
2. Credintials




'''