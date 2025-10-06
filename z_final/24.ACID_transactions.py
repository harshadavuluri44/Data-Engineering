'''

ACID properties that make Delta Lake (and other Lakehouse systems like Apache Hudi, Apache Iceberg) 
reliable, unlike a raw data lake.
-----------------------------------------------------------------------------------

1. ATOMICITY (A): A transaction is all-or-nothing.

    Either the entire write/update/delete succeeds, or none of it is applied.

Example: Writing 1M rows to a Delta table — if failure occurs halfway, no partial data is committed.
The transaction is rolled back.

-------------------------------------------------------------------------------------------------

2. CONSISTENCY (C): Data always moves from one valid state to another, following schema and 
                    constraints.

Example: If a column `amount` is defined as DOUBLE, we cannot insert a string value. All committed 
data must follow schema rules.

---------------------------------------------------------------------------------------------------

3. ISOLATION (I): Concurrent transactions do not interfere with each other.


Example: User A is reading the table while User B is updating it. 
        User A continues to see the old snapshot until User B's transaction is committed.

--------------------------------------------------------------------------------------------------

4. DURABILITY (D): Once a transaction is committed, it is permanently saved and will survive system
                    failures.


Example: A successful write to a Delta table is recorded in the transaction log. Even if the cluster
crashes, the data is still recoverable.

----------------------------------------------------------------------------------------------------

Why ACID is important for Lakehouses?

    Lakehouses store massive amounts of raw and structured data.  
    Without ACID, simultaneous reads/writes can lead to corrupted or inconsistent data.  
    ACID transactions enable safe updates, deletes, and merges on large datasets, ensuring 
reliability for analytics, BI, and ML workloads.

Examples: Delta Lake, Apache Hudi, Apache Iceberg

'''
