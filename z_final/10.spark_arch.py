'''

Apache Spark Architecture

Apache Spark follows a master-slave architecture consisting of 3 main components - 
Driver Program, Cluster Manager, and Executors.

Driver Program : Runs on master node and is responsible for overall execution of spark application.
It creates a SparkSession (which internally manages SparkContext) and converts the user code
into a logical execution plan, optimizes it, and constructs a DAG of stages. Each stage is further 
divided into tasks. The driver schedules tasks, tracks metadata, and collect results from executors.

Cluster Manager : Spark relies on a cluster manager like YARN, Mesos, kubernetes or Spark's built-in
Standalone manager to allocate CPU and memory resources to workers across the cluster.

Executors : Executors are worker processes launched on cluster nodes. They perform the actual
computation of tasks, cache data in memory/disk, and report results back to driver.

This architecture enables in-memory processing, distributed parallel execution, and fault tolerance 
via RDD lineage, makeing Spark much faster than traditional systems like Hadoop MapReduce.

'''