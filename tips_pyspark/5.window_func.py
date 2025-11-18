'''

we should do ordering during defining window itself


window_1 = Window.partitionBy('country').orderBy(col('total_watch_time').desc())


but not during apply rank and withColumn


'''