"""

Batch Processing:
    Processing data in large, finite chunks (batches) at scheduled intervals.
    Data is collected over a period of time and then processed together.

Example: A job scheduled at 2 AM every day loads data into a table.

-------------------------------------------------------------------------------------------------

Stream Processing:
    Processing data continuously in real-time as it arrives (on-demand).
    Data is handled record-by-record or in small windows of time.

Example: As data arrives in tools like Kafka, it gets processed into a table immediately.

------------------------------------------------------------------------------------------------

Key Differences:

Feature       | Batch Processing                          | Stream Processing
--------------| ----------------------------------------- | ------------------------------------------
Data Nature   | Finite, bounded datasets                  | Continuous, unbounded data
Latency       | High (data processed after collection)    | Low (near real-time processing)
Throughput    | High (large volumes processed at once)    | Steady (continuous ingestion and processing)
Scheduling    | Runs at scheduled intervals (e.g., daily) | Runs continuously as data arrives
Use Cases     | ETL jobs, nightly reports, data warehousing | Fraud detection, IoT sensor data, live dashboards

--------------------------------------------------------------------------------------------------

Summary:
    Use Batch Processing when data can be processed periodically and real-time results are not critical.
    Use Stream Processing when real-time insights and low-latency processing are required.

"""
