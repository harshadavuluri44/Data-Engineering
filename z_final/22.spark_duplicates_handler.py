'''

How to handle duplicates in Spark ?

--------------------------------------------------------------------------------------------------

1. Remove exact duplicates (all columns match)

df_d = df.dropDuplicates()

Removes all duplicates row by maintaing one occurence

--------------------------------------------------------------------------------------------------

2. Remove duplicates based on specific columns

df_d = df.dropDuplicates(['id','name'])

-------------------------------------------------------------------------------------------------

3. use distinct() for all columns

df_d = df.distinct()

Simpler and same as df.dropDuplicates() with all columns

------------------------------------------------------------------------------------------------

4. Keep the latest record when duplicates exist

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowspec = Window.partitionBy('id').orderBy(df['updated_at'].desc())

df_f = df.withColumn('row_num', row_number().over(windowspec)).filter('row_num==1').drop('row_num')

-------------------------------------------------------------------------------------------------

Depends the business logic

deduplication means removing the duplicates

'''