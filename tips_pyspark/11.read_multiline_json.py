'''

Multiline JSON :- There will be only one {} but keys/values are more than one line

Nested JSON :- There will be {} inside {}

---------------------------------------------------------------------------------------------------

Read Multiline JSON using PySpark


df = spark.read.option('multiline', 'true').json(file_path)

----------------------------------------------------------------------------------------------------

Read Multiline CSV using PySpark


df = spark.read.option('header', 'true') \
               .option('multiLine', 'true') \
               .csv(file_path)


'''

