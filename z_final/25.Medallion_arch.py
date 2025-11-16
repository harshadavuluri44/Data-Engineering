'''

MEDALLION ARCHITECTURE

A data design pattern widely used in modern data lakehouse platforms like Databricks to organize and
process data through progressive levels of refinement and quality.

--------------------------------------------------------------------------------

BRONZE LAYER (Raw Data):

    Landing zone for all raw, unprocessed data ingested from various sources.
    Data is stored in its original format with minimal transformation.
    Serves as the single source of truth.

Example: A table or data lake storing raw, unprocessed data.

--------------------------------------------------------------------------------

SILVER LAYER (Cleaned and Conformed):

    Intermediate layer containing cleaned, validated, and lightly transformed data.
    Removes duplicates, handles data quality issues, and applies business rules.
    Maintains detailed granularity.

--------------------------------------------------------------------------------

GOLD LAYER (Business-Ready):

    Final layer containing highly refined, aggregated, and business-ready datasets.
    Optimized for specific use cases like reporting, BI, or ML.

--------------------------------------------------------------------------------

Q. How do you qualify data from Bronze to Silver?

    Do NOT clean data in Bronze.
    Instead:
        1. Take raw Bronze data as input.
        2. Process/clean/transform it in your notebook or pipeline.
        3. Write the cleaned, validated result to the Silver layer.

--------------------------------------------------------------------------------

Example Steps:

Step 1: Read Bronze layer

bronze_df = spark.read.format('delta').load('data/bronze/customers')

Step 2: Clean / Transform

    a) Remove duplicates

    silver_df = bronze_df.dropDuplicates(['customer_id', 'product_id'])  
    # Maintain one row per customer-product combination

    b) Handle nulls

    silver_df = silver_df.fillna({'email': 'unknown@example.com'})
    silver_df = silver_df.filter(col('customer_id').isNotNull())

    c) Enforce schema / types

    from pyspark.sql.types import IntegerType
    silver_df = silver_df.withColumn('age', col('age').cast(IntegerType()))

    d) Validate business rules

    silver_df = silver_df.filter(col('age') > 10)

Step 3: Write to Silver Layer

silver_df.write.format('delta').mode('overwrite').save('data/silver/customers')

'''
