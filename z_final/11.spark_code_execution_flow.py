"""
Apache Spark Code Execution Flow

Step-by-step flow of how a Spark application executes:

-----------------------------------------------------------------------------------------------
1. Write Code:
      Write a Spark application in Python, Java, Scala, or SQL using RDDs, DataFrames/Datasets, or
      SparkSQL.

-----------------------------------------------------------------------------------------------
2. SparkContext / SparkSession Creation:
      When the program starts, it creates a SparkSession (which internally holds a SparkContext).
      Acts as the entry point to Spark, enables features like the Catalyst Optimizer through 
      DataFrame/SQL APIs, and negotiates resources with the Cluster Manager.

-----------------------------------------------------------------------------------------------
3. Build Logical Plan:
      Transformations (like .select(), .filter(), .join()) are lazy and not executed immediately.
      Spark builds a logical plan (a blueprint of operations to be performed on the data).

-----------------------------------------------------------------------------------------------
4. Catalyst Optimizer (for DataFrame / SQL / Dataset APIs):
      Logical plan passes through the Catalyst optimizer.
      Catalyst resolves references, applies optimization rules, and selects the optimal physical 
      plan.

-----------------------------------------------------------------------------------------------
5. DAG Creation:
      Spark converts the physical plan into a DAG (Directed Acyclic Graph) of stages.
      Each stage contains a set of pipelined transformations.

-----------------------------------------------------------------------------------------------
6. Job Launch (on Action):
      Nothing executes until an action is called (.collect(), .count(), .write(), etc.).
      Spark submits the DAG to the DAG scheduler.

-----------------------------------------------------------------------------------------------
7. DAG Scheduler:
      Splits the DAG into stages.
      Each stage is divided into tasks based on data partitions.
      Tasks are sent to the Task Scheduler for assignment to executors.

-----------------------------------------------------------------------------------------------
8. Execution on Executors:
      Executors (worker JVMs) execute the tasks.
      Read partitions from storage, perform transformations, spill to disk if needed, shuffle data
      between nodes, etc.

-----------------------------------------------------------------------------------------------
9. Result Back to Driver:
      Results of tasks are sent back to the driver program.

-----------------------------------------------------------------------------------------------
10. Task / Job Completion:
      Spark cleans up resources or launches the next stage of the job.
      Once all actions finish, the Spark application ends.

"""
