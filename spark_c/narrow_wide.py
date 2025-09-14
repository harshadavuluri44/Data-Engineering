'''

narrow :- Each task is performed or each partition is processed independently without requiring
data from other partitions - avoids shuffle
.withColumn(), .filter() etc

wide :- Each task is performed or each partition is processed once after data shuffling occurs
accross partitions
.groupBy(), join()

Diff 

1. narrow dont need shuffle
   wide needs shuffle 

2. narrow is fast and wide is slow due to shuffle
3. Fault tolerance :- narrow is fast recovered, wide is slowly recovered
4. narrow - constant memory usage
   wide - memory usage changes based on partition key or groupby key count and may cause OOM, data
   skew etc

'''