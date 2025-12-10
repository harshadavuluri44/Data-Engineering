'''
Suppose a critical KPI dashboard in Domo shows a sudden 15% drop in revenue for a specific region after
data migration from legacy IER AS400 system to Snowflake.

Walk us through how you would investigate and identify the root cause. What tools, queries, or checks
would you use?

------------------------------------------------------------------------------------------------------

STEP 1: Validate the COUNTS in SOURCE vs TARGET

Run the below query in SQL warehouses in respective tools

SELECT region, COUNTT(*), SUM(revenue)
FROM fact_revenue
WHERE region = 'Arizona'
AND revenue_date BETWEEN '2025-01-01' AND '2025-01-31'
GROUP BY region;

If Snowflake has fewer rows or smaller revenue when compared to legacy database, data was lost or
filtered incorrectly during migration

-------------------------------------

STEP 2: Check ETL Pipeline Logic (ADF/ Databricks) Follow 3 layers

Goal: Verify business rules weren't changed during migration.

Check 
    * Was any WHERE clause added/changed?
    * Were joins between facts and dims altered?
    * Was currency or timezone conversion introduced?
    * Did we exclude cancelled/ refunded orders ?

----------------------------------------

STEP 3: Validate Dimensions table perfectly

* Check if region codes changed
* Check whether all the mapping tables are perfectly used during migration
* check if region is changed to NULL by mistake which casuing rows to be dropped
* Currency conversion

------------------------------------------

STEP 4: Now move to DOMO

* Open the DOMO Dataset used for KPI card
* Compare its raw tables vs ETL output in snowflake
        Means source of DOMO vs tables in snowflake after migration
* Check filters applied in DOMO correctly or not
* Validate if any new logic was introduced in DOMO after migration

--------------------------------------------

STEP 5: Compare Revenue Before vs After Migration


SELECT 
    'AS400' AS source,
    SUM(revenue) AS total_rev FROM AS400_extract
    WHERE region = 'Arizona'
UNION ALL
SELECT
    'Snowflake' AS source,
    SUM(revenue) FROM fact_revenue
    WHERE region = 'Arizona'


If snowflake = AS400-15% -> migration caused the drop.



'''