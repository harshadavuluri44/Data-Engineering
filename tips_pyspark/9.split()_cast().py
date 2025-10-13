'''

df.withColumn('new_column', split(col('column'), '@')[1])

-------------------------------------------------------------------

column casting


df.withColumn('new_column', col('column').cast(int))


'''