'''

DIFFERENCES between RDD and DataFrame

1. No enforced schema for RDD, they are just Python objects
   Dataframes are structured with rows and columns as a table


2. Rdd operations are generally slower because they don't benefit from Spark's Catalyst Optimizer
   Data Frames are faster than RDD, code flow is optimized by catalyst optimizer

3. Easy to debug failures, as the code flow is not changed and executed as it is
   Difficult to debug, as code flow is changed by catalyst optimizer

4. Fault tolerance, they can easily recompute the lost partitions with the help of lineage
   Dataframes depends on rdd under the hood to acheive this behiavour

5. rdd are not benifited by tungesten engine
   df are benifited by tungesten engine

6. memory usage is more interms of rdd
   memory usage is very less (binary)

---------------------------------------------------------------------------------------------------

dataframes are immutable

Any transformation does not modify the original dataframe, instead it creates a new DataFrame with
applied changes
'''