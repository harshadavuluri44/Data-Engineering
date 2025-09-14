'''

Apache Spark Architecture

Apache Spark follows a master-slave architecture consisting of 3 main components - 
the Driver Program, the Cluster Manager, and the Executors.

Driver Program :
The driver runs on master node and is responsible for overall execution of spark application.
It creates a SparkSession (which internally manages SparkContext) and converts the user code
into a logical execution plan. This plan is then optimized and broken down into a DAG (Directed
Acyclic Graph) of stages. Each stage is further divided into tasks, which are the smallest
unit of execution. The driver also keeps track of metadata, schedules tasks, and collects
results back from executors.

Cluster Manager :
Spark doesn't manage cluster resources directly. Instead, it talks to a cluster manager like
YARN, Mesos or Spark's built-in Standalone manager. The cluster manager is responsible for
allocating resources (CPU, memory) across the cluster to spark application

Executors :
Executors are worker processes launched on cluster nodes. Each executor is responsible for
running tasks assigned by driver, storing data in memory or disk for caching, and reporting
status/results back to driver.

This architecture allows spark to achieve in-memory processing, fault tolerance (via RDD 
lineage), and distributed parallel execution, which makes it much faster than traditional
systems like Hadoop MapReduce.


Note :- Spark is doing everything inside driver program once SparkSession is created.
Spark’s internal components (SparkContext, DAG Scheduler, Task Scheduler) inside the driver.

'''