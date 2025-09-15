'''
BATCH Processing :- Batch Processing means processing data in large, finite chunks (batches) at
scheduled intervals.

Data is first collected and stored, then processed all at once.

Example :- Every night at 2AM, a job runs to process all sales transactions from previous day
and load them into delta lake.

* No new data is considered after the job starts - if more data comes later, run job again

Characteristics:

* High throughput (processes a lot of data at once)
* High latency - we dont get results until the whole job finishes
-----------------------------------------------------------------------------------------------------

Stream Processing :- Streaming processing means processing data continously in real-time as it 
arrives (like on-demand)


* Data source -> Kafka, Event Hubs, Kinesis, or files being written to a directory

Characteristics:
* Low latency - data is processed almost as soon as it arrives
* Suitable for real-time dashboards, fraud detections etc.
--------------------------------------------------------------------------------------------------

Differences

Data is processed in finite, bounded datasets
Uneven, continous data processing

Latency is high - takes time to ingest data into table
Latency is low  - Real time tables

Throughput is high bcz of large data should be processed
Throughput is steady due to continous ingestion



'''