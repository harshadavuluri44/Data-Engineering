'''

Pyspark dataframes are columns but not like constant variables.


So to add constant column


from pyspark.sql.functions import lit


df = df_1.withColumn('country', lit('USA'))


'''