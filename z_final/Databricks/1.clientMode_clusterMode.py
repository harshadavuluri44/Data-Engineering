'''

Client Mode = Interactive Notebook Runs

Cluster Mode = Scheduled Job Runs

--------------------------------------------------------------------------------------------------


Client Mode/ Interactive Work/ Notebooks/ Ad-hoc Runs


    Driver runs on the notebook-attached cluster's driver node

    Your browser session is tied to the driver.

    If session disconnects -> the job also stops

Used for
    Development, Testing, Debugging, EDA

-------------------------------------------------------------------------------------------------

Cluster Mode/ Job/ Workflow Runs

    Driver runs inside the cluster independent of your notebook

Used for
    Schedule ETL pipelines
    Production workloads

    Job continues even if we close our laptop


'''


