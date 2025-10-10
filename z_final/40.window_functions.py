'''

window functions in pyspark are used to perform calculations across set of rows related to current
row, without collapsing them into single row (unlike groupBy() aggregations)

-----------------------------------------------------------------------------------------

Example : Running Total

windowspec = Window.orderBy('order_date').rowsBetween(Window.unboundedPreceding, Window.CurrentRow)

df_running = df.withColumn('running_total', sum('amount').over(windowspec))

Window.UnboundedPreceding -> last row of partition
'''