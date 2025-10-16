'''

How do you handle data pipeline failures or latency issues?

---------------------------------------------------------------------------------------------------

1. Handling Data Pipeline Failures


A. Identify the failure

    Check logs, error messages

    Determine if failure is source-related, transformation-related, or target-related

B. Implement Retry Mechanisms

    For intermittent errors (network issues, API failures etc), implementing automatic retries.

C. Alerting & Monitoring

    Set up alerts using Databricks

    Notify responsible teams immediately

D. Graceful Handling

    Use staging tables or temporary storage to isolate failed records

    .option('mode', '{}')

    DROPMALFORMED : Spark skips any row that doesn't match the schema and they are not loaded into 
                    target table

    PERMISSIVE : Spark tries to parse every row, if data doesn't comply they are set to NULL and
                 optionally _corrupt_record column set to true and written to badRecordsPath

    FAILFAST : Spark stops processing immediately if malfromed row is encountered and Pipeline fails
               instantly.

    
    df = spark.read.option('header', 'true') \
                   .option('mode', "PERMISSIVE") \
                   .option('badRecordsPath', 'mnt/staging/bad_records')\
                   .schema(schema) \
                   .csv('file_path')

E. Rollback / Data Recovery

    Use Delta Lake Time travel or versioned table to restore previous state

    Maintain checkpointing incase of streaming processing (kafka)

    SELECT * FROM p1zenith_prospect.coremodel.fact_site_visit
    TIMESTAMP AS OF '2025-10-11 23:59:59'

--------------------------------------------------------------------------------------------------

2. Latency Issues (slow running Jobs)

A. Identify Bottlenecks

    Check slow transformations, large joins or inefficient queries

    Monitor compute resource utilization

B. Optimize ETL/ELT

    Partition tables and files for faster reads

    Use caching for repeated lookups

    Predicate pushdown and colum pruning

C. Scale Infrastructure

    For batch: Increase cluster size or use concurrent clusters

    For streaming: scale executors or parallelize partitions

D. Incremental Processing

    Avoid processing full datasets every run; use MERGE
'''