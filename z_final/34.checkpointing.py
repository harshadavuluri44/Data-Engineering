'''

What is Checkpointing in Spark?
-------------------------------------------------------------------------------------------------

It means saving RDD/DataFrame to a reliable storage(HDFS/S3/DBFS) so Spark can restart jobs without
recomputing the entire lineage.


Scenario

Spark keeps track of transformations using a lineage graph (DAG)

df1 -> df2 -> df3 -> df4 -> df5



If a failure happens at df5, Spark recomputes all previous steps from df1


This becomes slow or impossible when:

    The lineage is too long, etc.



Here checkpointing cuts the lineage and materializes the DF/RDD to reliable storage.

--------------------------------------------------------------------------------------------------

checkpointing   vs    cache/persist


data is stored in HDFS/S3/DBFS       data is stored in memory/RAM
used to retrieve lost data           used to reuse transformed data


'''

