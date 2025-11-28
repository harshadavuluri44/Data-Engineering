'''

What is Amazon RDS?


Amazon RDS, which stands for Amazon Relational Database Service, is a managed database service.


MANAGED - AWS takes care of scalability like increasing instances behind based on data we push,
                            security
                            configuration
                            Automatic Data backup
                            cross-region data replication


--------------------------------------------

Aurora DB is high performance based DB under RDS.

we need to mention engine type (Aurora) while creating DB under RDS


        Use Aurora when we need high performance, like incase of heavy traffic (
            Frequent/more INSERTS, DELETES, UPDATES)

-------------------------------------------------------------------------


RDS and Redshift both are used to store structured data.


RDS is like OLTP, use when

        frequent small reads/writes
        Low latency responses


Redshift is like OLAP, use when

        to store large historical data
        Long running analytical queries




'''
