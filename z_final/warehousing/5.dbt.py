'''

DBT (Data Build Tool)

Explain how DBT works end-to-end

DBT is a transformation framework that turns raw warehouse data into trusted, analytics-ready datasets
using SQL models.

End-to-End DBT works like:

1. It connects to data warehouse like (snowflake, Bigquery, Redshift, Databricks)

2. We write SQL models that define how data should be transformed.

3. DBT automatically builds a DAG based on ref() we defined in SQL models.

4. When we run DBT, it:
    Executes models in correct dependency order
    Materializes them as tables/views/incremental models
    Applies test, documentation, and freshness checks
    Uses macros/Jinja to keep logic reusable

5. Finally, DBT produces clean, governed, version-controlled datasets ready for analytics or machine
   learning.

-----------------------------------------------------------------------------------------------------

Where dbt fits in the ELT pipeline

ELT = Extract -> Load -> Transform

* Extract/Load -> Done by tools like Databricks etc.

* Transform  -> Done by dbt

dbt takes raw loaded tables and converts them into clean business-ready tables.

---------------------------------------------------------------------------------------------------

What is the role of staging, intermediate, and mart layers?

1. staging layer (stg_)

Purpose:
    clean and standardize raw source data
    Rename cryptic columns
    Apply light transformations (type casting, trimming)
    Introduce business-friendly column names

2. Intermediate Layer (int_)

Purpose:
    Join multiple staging tables
    Apply business logic
    Handle Slowly changing dimensions
    Create reusable intermediate datasets

3. Mart Layer (fact_,dim_)

Purpose:
    Final analytics-ready datasets
    Facts and dimensions for BI,ML, dashboards
    Business KPIs and derived metrics
    Low-grain tables optimized for consumptions

--------------------------------------------------------------------------------------------------

Difference between View, Table, Incremental, and Emphemeral Models in DBT

1. View

    DBT creates a SQL view in the warehouse
    Everytime you query it, Snowflake re-runs the underlying SQL

2. Table

    DBT runs SQL and stores results as a physical table
    Data is only refreshed when dbt rebuilds it

3. Incremental

    Like a table, but DBT only processes new or changed records instead of full refresh.

    MERGE operation

---------------------------------------------------------------------------------------------------

How do you handle schema changes in DBT incremental Models?

Unlike PySpark, DBT doesn't have .mergeSchema or .overwriteSchema.

DBT is SQL-based - So handle schema changes using config + SQL logic + data warehouse features like
MERGE


Strategy 1 :  on_schema_merge

on_schema_merge = ignore -> ignore new columns
                  append_new_columns -> only add new columns
                  sync_all_columns -> add & drop columns to match model.


We might use CASE WHEN THEN ELSE END (similar if else)`

use COALESCE() to default value for null valued columns

-----------------------------------------------------------------------------------------------------

How does DBT manage dependencies?

ref() functions tells which model depends on which other model.
in what order models should run


DBT manages dependcies through the ref() function. When one model refrences another using ref(),
DBT understands that the refrenced model must run first.

DBT uses these ref() relationships to automatically buil a DAG - a Directed Acylic Graph that
determines order of execution, ensures proper lineage.

-------------------------------------------------------------------------------------------------

How do you test data quality in DBT?


DBT tests data quality using two types of tests: generic and custom.

Generic tests like unique, not_null, accepted_values, and relationships are defined in YAML and
automatically complied into SQL

For more complex rules, We write custom tests either as SQL files or YAML-based custom test that
retrun invalid records.


Tests in DBT run at model boundaries because a model must be materilaized before it can be validated.

DBT runs on raw data, so there will be no use of running test at the start of models.

'''