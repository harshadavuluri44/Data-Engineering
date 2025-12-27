
Features of pyspark
----------------------------------------------------------------------------------------------------

In-Memory Computation :-
    Pyspark processes data in memory (RAM) instead of reading from disk every time, which significantly imporves performance for iterative or repated operations like aggregations and ML

    * Disk I/O operations is slow and expensive compared to RAM
    * RAM is much faster, so storing intermediate results in memory speeds up iterative operations like aggregations or ML

    How it works in pyspark?
    * RDDs/DataFrames are stored in memory using .cache() or .persist()
    * When an action like .count() or .collect() is triggered:
       -> Pyspark executes the transformation logic once,
       -> If .cache() or .persist() is used stores the result in memory(on executors),
       -> and resues that results for further actions.

--------------------------------------------------------------------------------------------------

LAZY EVALUATION - PySpark use lazy evaluation, which means transformations are not executed immediately.
    Instead they are recorded as a plan to be executed only when an action is called.

    * Transformations - These are lazy operations that define a logical plan of what needs to be done.
      - Pyspark does not execute them immediately - it simply builds a chain of tansformations 
      - My instructions like .filter(), .select(), .map()
    * Actions - These are eager operations that trigger the execution of the entire computation.
      - When an action is called, PySpark looks back at all previous transformations to execute the computation pipeline.
      - the "Go!" command like .show(), .collect(), .count()

    Pyspark does NOT execute transformations immediately. It just remembers what needs to be done like a plan

    It only executes everything in one go, efficiently, when an action is called.

    Working :-

    * Every time we write a transformation (filter, select, join etc) it draws a box and an arrow to the next box
    * This builds a Directed Acyclic Graph(DAG) - a flowchart of what operations to perform
    * Only when you say "Do it!" (via .collect() or .show()), it:
        -> Looks at the whole board(DAG)
        -> Optimizes the route (By Catalyst optimizer)
        -> Executes efficiently


    Once action is triggered, PySpark passed DAG to Catalyst optimizer(builds the optimized logical plan/DAG) - DAG scheduler executes the plan i.e DAG scheduler  breaks into stage and tasks - These tasks are sents to executors(worker noeds) for actual computation

Final High level understanding of Lazy Evaluation :- Transformations in PySpark are not executed immediately. Instead, they are recorded as a chain of operations, forming a Directed Acyclic Graph (DAG). When an action is called, the Catalyst Optimizer generates an optimized logical plan from this DAG. The optimized plan is then executed by the DAG Scheduler, which breaks it into stages and tasks to run on executors.

--------------------------------------------------------------------------------------------------

Inbuilt Optimization in PySpark :- PySpark achieves high performance through 2 core optimization components

1. Catalyst Optimizer - Query plan optimization (Available only on driver node)
    * A rule-based and cost-based optimizer for DataFrame and SQL queries
    * Transforms high-level code/ DAG into an optimized logical and physical plan
    * Applies techniques like 

2. Tungsten Engine - Physical execution optimization (Available on both driver and worker nodes)
    * Optimizes memory and CPU efficiency at physcial execution level
    * Compiles whole  stage code to java bytecode

---------------------------------------------------------------------------------------------------

Immutable :- A core concept that ensures safety, reliability & fault tolerance in distributed computing.
    
    Immutability :- * In PySpark DataFrames and RDDs are immutable - means that once created, they cannot be changed directly.

    * Any transformation(like .filter(), .select(), etc.) does not modify original DataFrame, Instead it returns a new DataFrame with the transformation applied

    How immutability helps Spark: * Spark builds a lineage - a logical plan of all transformations applied to data.

    * If a node fails or data is lost during computation, Spark can recompute the lost data using this lineage (because the original data hasn't changed)

    * This makes Spark highly resilient and fault-tolerant without needing to store interediate data physically

    NOTE :- Unlike Pandas, PySpark does not support in-place operations.
    There is no inplace=True parameter in PySpark methods - everything returns a new DataFrame

-----------------------------------------------------------------------------------------------------

Fault Tolerant :- If something goes wrong(like a node crashes or a task fails), Spark can recover and still finish the job correctly, without restarting everything from the beginning.
    Q. How Does PySpark achieve fault tolerance?
    A. 1.RDD/DF Lineage :- PySpark remembers the entire chain of transformations(like filter, map, join) through something called lineage
    If a partition of data is lost, Spark does not need to re-read everything - it just recomputes that part from the original data + transformations

    Example :- df = spark.read.csv("data.csv)
               df2 = df.filter("age>30").select("name)

    If a worker that was processing df2 crashes : Spark uses the lineage from df -> filter() -> select() to recompute only the lost data.

    2. Data Replication :- During wide transformations (like join, groupBy, distinct), Spark performs a shuffle, where data is repartitioned across nodes.

    Spark write intermediate shuffle files to local disk

    If a worker fails after writing those files, Spark can re-fetch them from another node or recreate them using lineage - not from scratch,

-----------------------------------------------------------------------------------------------------

Cluster managers in PySpark :- A cluster manager is like boss of the Spark ecosystem. It is responsible for 1. Allocating resources (CPU, memory) across the cluster
    2. Launching executors(worker nodes)
    3. Scheduling tasks
    4. Monitoring job execution
    5. Handling failures

Why does PySpark need a cluster manager?
PySpark(which runs on top of Apache Spark) doesn't manage resources or machines on it own. It relies on a cluster manger to : 1. Launch and manage worker nodes
                      2. Distribute tasks across available machines
                      3. Monitor rask health and retry if needed
                      4. Ensure efficient usage of CPU, memory, and disk
                    
Cluster Managers supported by PySpark :- 1. Spark Standalone - Spark's built-in cluster manager
                                         2. Apache Mesos
                                         3. Hadoop YARN
                                         4. Kubernetes - Modern container-based cluster manager. Great for cloud-native deployments and auto scaling
                                
spark = SparkSession.builder.master("yarn").appName("test_harsha").getOrCreate()

-----------------------------------------------------------------------------------------------------