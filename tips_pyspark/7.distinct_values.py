'''

count no.of distinct values in a column


from pyspark.sql.functions import countDistinct


# we should wrap countDistinct always in select or agg during groupBy

df_1 = df.select(countDistinct('col_name'))

'''