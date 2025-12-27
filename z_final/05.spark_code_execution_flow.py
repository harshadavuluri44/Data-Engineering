'''

Apache Spark Code Execution Flow

-------------------------------------------------------------------------------------------------

1. Write Code
2. SparkSession / SparkContext Created
3. Logical Plan is Created by Catalyst Optimizer
4. Action Triggered → Job Creation:
      - Catalyst Optimizer → Optimized Logical Plan
      - Physical Plan Created (Catalyst Planner)
5. DAG Scheduler:
      - Identifies shuffle boundaries
      - Splits the physical plan into stages (DAG of stages) for each job
      - Creates tasks inside each stage (one per partition)
      - Sends tasks to Task Scheduler
6. Task Scheduler:
      - Assigns tasks to executors
      - Handles task retries
7. Executors:
      - Read data from storage
      - Execute transformations
      - Shuffle / spill / aggregate / compute
      - Write output or return result
8. Results returned to Driver
9. Job Completed

  
--------------------------------------------------------------------------------------------------
      
Q.    Explain what happens when you run this PySpark code:
      
      df.read.parquet() → filter() → groupBy() → write.parquet()



      In the first one, spark reads the metadata and adds it into logical plan
      (No data is loaded into memory yet)

      2nd, 3rd transformations are also added into logical plan
      (spark continues building DAG)

      4th one  action, once triggered, spark convertes logical plan into optimal physical
      plan and reads only required data based on filtes and do grouping, then writes 
      data to storage/table

'''
