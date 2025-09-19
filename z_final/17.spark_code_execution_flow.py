'''
1. Write code

   write a Spark application in Python/ Java/ Scala/ SQL using RDDs or DataFrame/ Datasets/ SparkSQL

2. Spark Context/Session Creation

   When above program starts, it creates a SparkSession (which internally holds a SparkContext) - this
   acts as the entry-point and negotiates resources with cluster manager.

3. Build Logical Plan

   As above application apply transformations (like .select(), .filter(), .join()), Spark does run
   them immediately

   It builds a logical plan (a blueprint of operations to be done on the data)

4. Catalyst optimizer (only for DataFrame/ SQL/ Dataset APIs)

   Spark sends the logical plan through catalyst optimizer

   Catalyst resolves it, applies optimization rules, and chooses the optimal physical plan

5. DAG Creation

   Spark converts the above physical plan into a DAG of stages.

   Each stage is set of pipelined transformations

6. Job Launch (on Action)

   Nothing is executed until an action is called (.collect(), .count(), .write())

   Spark then submits DAG to the DAG scheduler.

7. DAG scheduler

   DAG scheduler splits the DAG into stages and then into multiple tasks based on data partitions

   Tasks are sent to the Task Scheduler, which assigns them to executors.

8. Execution on exectors

   Executors (worker JVMs) run the tasks.

   They read partitions from storage, perform transformations, spill to disk if needed, shuffle data
   between nodes, etc.

9. Result back to driver

   Results of tasks are send back to driver program

10. Task/ Job completion

    Spark cleans up resources or launches next stage of Job

    once all actions finish, your spark application ends

'''