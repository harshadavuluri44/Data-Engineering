'''

JOB : A job in Spark is the execution of the DAG corresponding to an action. It is triggered when an
     action is called on a DataFrame or RDD.


Each job is divided into stages, and each stage contains tasks that run in parallel on partitions

------------------------------------------------------------------------------------------------

STAGE : A stage is set of tasks that can execute together without causing shuffle. Wide operations
end the current stage and cause a shuffle to create new stage

SO ->  stage 1 -> shuffle -> stage 2

-----------------------------------------------------------------------------------------------

TASK : The smallest unit of work in Spark, which applies the transformations and operations defined
in Spark code to one and each partition of data

'''