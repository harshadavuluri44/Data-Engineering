'''
A partition in spark's in memory or worker node's memory can contain different partition
column values.
----------------------------------------------------------------------------------------

Data skew means partition having large data compared to other
Which leads to uneven task execution, i.e few tasks take more time to complete results in
increase in whole spark execution time.

Ways to fix it

1. repartition
2. salting keys


'''