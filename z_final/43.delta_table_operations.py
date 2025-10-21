'''

1. Create Delta Table

    CREATE TABLE IF NOT EXISTS p1zenith_prospect.coremodel.dim_brand(brand_id INT, brand_desc STRING)
    USING DELTA
    LOCATION 's3://pcp-prod-us-east-1-data/warehouse/p1zenith_prospect/coremodel/dim_brand'


    df.write.format('delta') \
    .option('path','s3://pcp-prod-us-east-1-data/warehouse/p1zenith_prospect/coremodel/dim_brand')
    .saveAsTable(p1zenith_prospect.coremodel.dim_brand)

--------------------------------------------------------------------------------------------------

2. Read or Load Delta Table

    df = spark.read.format('delta').load(storage_location)

    df = spark.read.table('p1zenith_prospect.coremodel.dim_brand')

--------------------------------------------------------------------------------------------------

3. Write or Append data

    df.write.format('delta').mode('append').saveAsTable('p1zenith_prospect.coremodel.dim_brand')

-----------------------------------------------------------------------------------------------------

4. Optimize and Vacuum

    OPTIMIZE p1zenith_prospect.coremodel.dim_brand

    VACUUM p1zenith_prospect.coremodel.dim_brand RETAIN 168 HOURS

    OPTIMIZE p1zenith_prospect.coremodel.dim_brand
    ZORDER BY (id)

------------------------------------------------------------------------------------------------

5. Schema Evolution/ Merge Schema

    df.write.format('delta').option('mergeSchema', 'true') \
            .mode('append')
            .saveAsTable('p1zenith_prospect.coremodel.dim_brand')
'''