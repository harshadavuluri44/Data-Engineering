'''

Aggregate multiple columns in single group BY

from pyspark.sql.functions import sum, col

df_1 = df.groupBy('customer_id').
        agg(sum(col('amount')).alias('total_purchase'),sum(col('refund_amount')).alias('total_refund'))


note : do both aggregations inside single agg() function,

instead

dont create .agg()  . agg() twice for both
'''