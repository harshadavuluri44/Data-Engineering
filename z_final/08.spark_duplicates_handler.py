'''

How to handle duplicates in Spark ?

DEDEPULICATION means removing the duplicates.

--------------------------------------------------------------------------------------------------

1. Using dropDuplicates()

# Drop all exact duplicate rows
df_d = df.dropDuplicates()


# drop duplicates based on specific columns

df_d = df.dropDuplicates(['id','name'])

-------------------------------------------------------------------------------------------------

2. Using distinct()

# Drop all exact duplicate rows, works same as df.dropDuplicates()
df_d = df.distinct()

------------------------------------------------------------------------------------------------

3. Using Window and row_number()

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowspec = Window.partitionBy('id','name').orderBy(df['updated_at'].desc())

df_f = df.withColumn('row_num', row_number().over(windowspec)).filter('row_num==1').drop('row_num')

-------------------------------------------------------------------------------------------------

NOTE - In data processing, use Delta Lake MERGE INTO instead of .mode('append') to avoid NULLS

-----------------------------------------------------------------------------------------------


Among the above ways, which is more efficient and why?


dropDuplicates() is Most efficient -

    Uses optimized aggregation by dropping duplicates across the each partition first.

distinct() does global distinct for each row across all partitions.

window() involves shuffling + sorting + windowing

'''