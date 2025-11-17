'''

WHAT is SPARK SQL?

Spark SQL is a module in Apache Spark that allows to query structured data using SQL syntax

It works on DataFrames and Datasets, enabling us to run SQL queries directly on Spark data.

-------------------------------------------------------------------------------------------

USING DataFrame API

from pyspark.sql.functions import col, sum

df = spark.createDataFrame([(1,'Alice',3000), (2,'Bob',4000)], ['id','name','salary'])

df.select(col('name'), col('salary')*1.1).show()

df.groupBy('name').agg(sum(col('salary')).alias('total_salary')).show()

------------------------------------------------------------------------------------------------

USING SPARK SQL

# Register DataFrame as a temporary table/ view   (MANDATORY)

df.createOrReplaceTempView('employees')

spark.sql('SELECT name, salary*1.1 AS updated_salary FROM employees).show()

spark.sql('SELECT name, SUM(salary) AS total_salary FROM employees GROUP BY name').show()

----------------------------------------------------------------------------------------------------

Spark SQL queries also benfit from Catalyst Optimization, just like DataFrame API.

'''