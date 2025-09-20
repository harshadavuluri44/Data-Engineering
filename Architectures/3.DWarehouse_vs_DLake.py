'''

Data Warehouse vs Data Lake

    Structured
    Structured + semi-structured + unstructured

    Enforces schema-on-write (schema should be defined and data to be written comply to schema)
    complies to schema-on-read

    Optimized databases (Redshift, snowflake, Bigquery) Storage depends on cluster size defined
    Cheap, Scalable object storage (S3, ADLS, GCS)

Felxibility - Rigid schema
              Very high (store anything)

Cost  - Higher storage cost but optimized queries
        Low storage cost, high query cost

'''