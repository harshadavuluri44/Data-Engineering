'''
BATCH Processing :- Batch Processing means processing data in large, finite chunks (batches) at
scheduled intervals.

Stream Processing :- Streaming processing means processing data continously in real-time as it 
arrives (like on-demand)
--------------------------------------------------------------------------------------------------

Differences

Data is processed in finite, bounded datasets
Uneven, continous data processing

Latency is high - takes time to ingest data into table
Latency is low  - Real time tables

Throughput is high bcz of large data should be processed
Throughput is steady due to continous ingestion

A job shceduled at 2AM every day loads data into table
As data arrives to tools like KAFKA, data gets processing into table

'''