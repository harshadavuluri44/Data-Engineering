'''
Transformations - Operations that create a new RDD/DataFrame from an existing one.

i) Lazy - They don't execute immediately, instead Spark just builds a logical plan (DAG)
ii) Actual execution happens only when an action is called.

.filter, .withColumn, .groupBy, .join

Actions - Operations that trigger execution of DAG and return value to driver program or write
data to storage

i) Eager - They cause spark to compute the result of transformations

.show(), .count(), .collect()
df.write.mode().saveAsTable()

'''