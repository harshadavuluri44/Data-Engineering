"""
Apache Spark Architecture

Apache Spark follows a master-slave architecture consisting of three main components:
Driver Program, Cluster Manager, and Executors.

-----------------------------------------------------------------------------------------------
1. Driver Program:

    Runs on the master node and is responsible for the overall execution of the Spark application.
    Creates a SparkSession (which internally manages SparkContext).
    Converts user code into a logical execution plan, optimizes it, and constructs a DAG of stages.
    Each stage is further divided into tasks.
    The driver schedules tasks, tracks metadata, and collects results from executors.

-----------------------------------------------------------------------------------------------
2. Cluster Manager:

    Allocates CPU and memory resources to worker nodes across the cluster.
    Spark can use different cluster managers:
        YARN
        Mesos
        Kubernetes
        Spark's built-in standalone manager

-----------------------------------------------------------------------------------------------
3. Executors:

    Worker processes launched on cluster nodes.
    Perform the actual computation of tasks.
    Cache data in memory/disk when needed.
    Report task results back to the driver.

-----------------------------------------------------------------------------------------------
Key Benefits of Spark Architecture:

    In-memory processing for faster computation.
    Distributed & parallel execution across nodes.
    Fault tolerance via RDD lineage.
    Much faster than traditional systems like Hadoop MapReduce.

"""