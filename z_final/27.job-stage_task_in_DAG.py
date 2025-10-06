'''

JOB:

     A job in Spark is the execution of the DAG corresponding to an action.
     It is triggered when an action (like `count()`, `collect()`, `write()`) is called on a DataFrame
     or RDD.
     Each job is divided into stages, and each stage contains tasks that run in parallel on partitions.

--------------------------------------------------------------------------------------------------

STAGE:

     A stage is a set of tasks that can execute together without causing a shuffle.
     Wide transformations (like join, groupBy) end the current stage and trigger a shuffle to 
     create a new stage.

Example: 
    stage 1 -> shuffle -> stage 2

-------------------------------------------------------------------------------------------------

TASK:

     The smallest unit of work in Spark.
     Applies the transformations and operations defined in Spark code to one partition of data.

--------------------------------------------------------------------------------------------------

'''
