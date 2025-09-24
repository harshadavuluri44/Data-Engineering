'''

ACID properties which make Delta Lake (or other Lakehouses like Apache Hudi, Apache Iceberg) 
reliable, unlike a raw data lake


1. ATOMICITY (A) : A transaction is all-or-nothing

    Either the entire write/update/delete succeeds, or nothing happens

Example : When writing 1M rows to a Delta table - if failure occurs halfway, no partial data is 
committed



2. CONSISTENCY (C) : Data always moves from one valid state to another, following the schema &
constraints.

Example : A column amount is defined as DOUBLE -> we can't accidentally insert a string

All committed data is consistent with schema rules.



3. ISOLATION (I) : Concurrent transactions don't interfere or affect with each other.

Example : User A is reading table while User B is updating it -> User A sees the old snapshot untill
User B's write is committed


4. DURABILITY (D) : Once a transaction is committed, it is permanently saved and cannot be lost even
if there is a system crash

Example : A successful write to a Delta table is persisted in the transaction log, so it will survive
cluster failures.

-----------------------------------------

Why ACID are important for Lakehouse ?

Lakehouses store massive amounts of raw and structured data. Without ACID support, simultaneous
reads/writes could lead to corrupted or incosistent data

ACID transactions allow safe updates, deletes and merges on large datasets, enabling reliable
analytics, BI and ML workloads

Examples : Delta Lake, Apache Hudi and Apache Iceberg
'''