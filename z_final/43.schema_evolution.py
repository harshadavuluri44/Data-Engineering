'''

How do you handle schema evolution in Delta Lake and Databricks ETL jobs?

--------------------------------------------------------------------------------------------

df.write.format('delta').mode('append').option('mergeSchema','true').save('storage_loc')

df.write.format('delta').mode('overwrite').option('overwriteSchema','true').save('storage_loc')



'''