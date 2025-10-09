'''

In pyspark, we can get IF ELSE using .when()

from pyspark.sql.functions import when



df = df.withColumn('updated_points',
                when(col('net_spending') > 4000, col('loyalty_points') * 1.1)   # Rule 1
               .when(col('net_spending') < 1000, col('loyalty_points') * 0.95)  # Rule 2
               .otherwise(col('loyalty_points'))                                 # Default
)
'''