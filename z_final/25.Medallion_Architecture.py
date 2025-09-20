'''

MEDALLION ARCHITECTURE

It is a data design pattern widely used in modern data lakehouse platforms like Databricks to 
organize & process data through progressive levels of refinement and quality.


BRONZE LAYER (Raw Data) : 

    This is landing zone for all raw, unprocessed data ingested from various sources. Data here is
stored in its original format with minimal transformation, serving as the single source of truth.


Ex : It's a table or data lake where we store raw, unprocessed data


SILVER LAYER (Cleaned and Conformed) :

    This intermediate layer contains cleaned, validated, and lightly transformed data. 
    
It removes duplicates, handles data quality issues, and applies business rule while maintaining
detailed granularity.



GOLD LAYER (Business-Ready) :

    The final layer contains highly refined, aggregated, and business ready datasets optimized for
specific use cases


--------------------------------------------------------------------------------

Q . How do you qualify data from Bronze to Silver?

    -   It does not mean you clean data in Bronze.

    Instead, it means:
        Take raw Bronze data as input
        Process/clean/transform it in your notebook or pipeline
        Write cleaned, validated result to Silver layer


A.  

Step 1 : Read Bronze layer

bronze_df = spark.read.format('delta').load('data/bronze/customers')

Step 2 : Clean / Transform

    a) Remove duplicates

    silver_df = bronze_df.dropDuplicates(['customer_id'])

    b) Handle nulls

    silver_df = silver_df.fillna({'email':'unkown@example.com'})

    silver_df = silver_df.filter(col('customer_id').isNotNull())

    c) Enforce schema/type

    silver_df = silver_df.withColumn('age', col('age').cast(IntegerType()))

    d) Validate business rules

    silver_df = silver_df.filter(col('age') > 10)


Step 3 : Write to Silver Layer

silver_df.write.format('delta').mode('overwrite').save('data/silver/customers')


'''