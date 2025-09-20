'''

WHAT is a DATA WAREHOUSE?

A Data Warehouse is a centraliazed repository that stores integrated data from multiple sources,
optimized for analytical queries and reporting. Unlike operational databases designed for
transactions, data warehouses are built for complex queries across large datasets.

--------------------------------------------------------------------------------------------

CORE ARCHITECTURE COMPONENTS

1. DATA SOURCE LAYER :- They may be OLTP Databases like MYSQL etc, 
                     External APIs and web services
                     Flat files (CSV, JSON, XML)

    

2. DATA INTEGRATION LAYER (ETL/ELT) :- The extraction, transformation, and loading process that moves
data from source layer to warehouse

Modern architectures often use ELT where raw data is loaded first, then transformed within the
warehouse using its computational power

3. STORAGE LAYER :- The actual data warehouse database, where our data resides. Typically organized in
one of these schemas

* star schema : Central fact table sorrounded by dimension tables
* snowflake schema : Normalized version of star schema

4. PRESENTATION LAYER :- Tools and interfaces that end users interact with
                            - BI dashboards
                            - Analytics platforms etc

                            
EXAMPLES OF Data Warehouses :- Snowflake, Amazon Redshift, Google BigQuery




'''