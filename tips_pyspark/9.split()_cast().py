'''

df.withColumn('new_column', split(col('column'), '@')[1])

--------------------------------------------------------------------------------------------------

column casting  (No need to import of cast() function, it is part of col())


from pyspark.sql.functions import IntegerType, col


.cast('int') and .cast(IntegerType())    ->    Both are same


df.withColumn('new_column', col('column').cast('int'))

df.withColumn('new_column', col('column').cast(IntegerType()))





'''