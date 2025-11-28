'''

to_date() in PySpark is used to convert a string column into Date type


NOTE - to_date() always returns date in yyyy-mm-dd format and expects yyyy-mm-dd/ yyyy/mm/dd format

---------------------------------------------------------------------------------------------------
SYNTAX

from pyspark.sql.functions import to_date


df = df.withColumn('order_date', to_date('order_date'))

    If the string is in yyyy-mm-dd

    else

        df = df.withColumn('order_date', to_date('order_date', 'dd/MM/yyyy'))

'''