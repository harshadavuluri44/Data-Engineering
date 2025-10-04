'''


Transformations: Operations that create a new RDD/DataFrame from an existing one.

    Lazy: They don't execute immediately; Spark builds a logical plan (DAG).
    Execution: Happens only when an action is called.

Examples: .filter(), .withColumn(), .groupBy(), .join()

--------------------------------------------------------------------------------------------------

Actions: Operations that trigger execution of the DAG and return results to the driver or write 
data to storage.

    Eager: They force Spark to compute the result of all preceding transformations.
    Execution: Triggered immediately.

    Examples: .show(), .count(), .collect(), df.write.mode().saveAsTable()

----------------------------------------------------------------------------------------------------

'''