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


4. DURABILITY (D) : Once a transaction is committed, it is permanently saved, even if there is a 
system crash

Example : A successful write to a Delta table is persisted in the transaction log, so it will survive
cluster failures.
'''