'''

datediff(start_date, end_date)


It is used to calculate diff between 2 date columns

---------------------------------------------------------------------------------------------

from pyspark.sql.window import Window
from pyspark.sql.functions import lag, datediff, col

window = Window().partitionBy('customer_id').orderBy('txn_date')

df_1 = transactions_df.withColumn('prev_txn_date', lag('txn_date', 1).over(window))

df_2 = df_1.withColumn('days_of_gap', datediff(col('txn_date'),col('prev_txn_date')))

df_3 = df_2.fillna({'days_of_gap':0})
df_4 = df_3.filter(df_3.days_of_gap>30)
df_4.select('customer_id', 'days_of_gap').show()

'''