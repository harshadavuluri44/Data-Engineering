'''
Flow of DBX cluster (DBR 15.4, 4 worker nodes, i3.xlarge) Spin up -> pyspark notebook execution ->
cluster termination

CLUSTER CONFIGURATION RECAP:

* DBR VERSION  : 15.4 (Databricks Runtime with pre-installed Spark, JVM, Python, Delta Lake, etc.)
* Driver node  : i3.xlarge (4 vCPUs, 30.5GB RAM)
* Worker nodes : 4 nodes of i3.xlarge (each also 4 vCPUs, 30.5GB  RAM)

STEP-BY-SETP EXECUTION FLOW:

User Starts Cluste

1. Databricks interacts with the underlying cloud provider (AWS) to:
    * Provision 1 i3.xlarge instance of Driver
    * Provision 4 i3.xlarge EC2 instances for Workers

2. Each instance is a VM (with Linux OS + Spark environment preconfigured).

3. The DBR 15.4 image is loaded onto all nodes i.e Virtual Machines
    Recall :- image has spark, JVM, Python, Delta Lake etc.

4. All 5 nodes boot up with required software stack:- Java 11, Python 3.x, Spark 3.x, Delta Lake etc

5. The Driver node intializes the SparkContext and contacts Databricks control plane to register
   the cluster
   
6. Each worker node launches a JVM process and registers a Spark Executor.

7. Each i3.xlarge Worker node typically gets:
    * ~27 GB usable memory (after JVM overhead)
        - 3.5 GB goes for JVM overhead (i.e JVM internals, garbage collection, shuffle operations,
          tungesten engine etc....)
    * 4 available task slots (1 per vCPU)
        - 1vCPU runs only 1 task a time (No multithreading at task or CPU level)

    So we get 16 tasks slots total (4 workers * 4 vCPus)

EXECUTION PART :-

After the cluster setup is complete and the notebook is attached to the cluster, the Python code
runs on the Driver node, which creates or uses an existing SparkSession.

When Spark code is executed, the Driver parses (NOTE :- INSIDE DRIVER JVM does this ->) it and 
constructs a logical plan. This plan is analyzed and optimized by Catalyst, producing an optimized
logical plan and then a physical plan.

The DAG Scheduler then breaks the physical plan into stages, based on shuffle boundaries. 
Each stage is further divided into tasks.

These tasks are sent from the Driver to EXECUTORS RUNNING ON THE WORKER NODES, where the actual 
computation is performed.

Once the tasks complete, the results are returned to the Driver, where the final output is 
collected or further processed.

------------------------------------------------------------------------------------------------
Here lets explore more about 6th point - JVM process - registers a Spark Executor

When VM(worker) spins up :
    * It has Linux + Spark binaries installed (as part of DBR)
    * It launches a JVM process dedicated to running Spark tasks

What is a JVM process?

* JVM = Java Virtual Machine
* Spark is written in Scala (scala code runs on JVM), so Spark needs JVM to run
* On each worker, a JVM is started that acts as a Spark Executor

* Spark Executor is launched inside the JVM (JVM based daemon process)
* It is responsible for:
    * Running tasks sent by the Driver
    * Storing data in memory/disk
    * Communicating back with the Driver

* Once the Spark Executor starts : It contacts the Driver to say : 
    " Hey, I'm ready! you can assign tasks to me."

'''