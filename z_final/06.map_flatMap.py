'''

1. map() - Transformation
    
    Applies a function to each element of RDD/ DataFrame
    Output : one element per input element (1-to-1 mapping)

syntax :- rdd.map(func)

Example:
rdd = [1,2,3]
mapped_rdd = rdd.map(lambda x:[x,x*2])
Output -> [[1,1],[2,4],[3,6]]

----------------------------------------------------------------------------------------------

2. flatMap() - Transformation

    Works same as map, applies a function to each element
    But function can return multiple elements (or none)
    Output :- flattened list of results

Example:
rdd = ['hello world', 'spark rdd']
flatted_rdd = rdd.flatMap(lambda line: line.split(" "))
Output -> ['hello', 'world', 'spark', 'rdd']

DIFF B/W MAP() AND FLATMAP() IN SPARK

1. Output per input - exactly 1 in map()
                      0 or more in flatmap()

2. Data Structure - map() keeps nested structure (ex: list of lists)
                    flatMap() flattens results into single sequence

3. Use Case - map() transforms each element
              flatMap() split/ explode elements

----------------------------------------------------------------------------------------------

3. mapPartitions() - Transformation

    Applies function to each partition independently (instead of each element)
    Useful when expensive setup needs to be done once per partition

mapped_rdd = rdd.mapPartitions(func)

mapPartitions is like flatMap, it can return multiple elements and a flattened result

----------------------------------------------------------------------------------------------

4. groupByKey() - Transformation

    Groups all values for each key together 
    Similar to groupBy in dataframe
    Causes full shuffle (expensive)

Example:
rdd = [('a',1), ('b',6), ('a',3), ('c',7), ('a',9)]
grouped_rdd = rdd.groupByKey()
Output -> [('a',[1,3,9]), ('b',[6]), ('c',[7])]

----------------------------------------------------------------------------------------------

5. reduceByKey() - Transformation

    Aggregates values for each key using reduce function
    Performs local aggregation (combiner) before shuffle
    More efficient than groupByKey()

Example:
rdd = [('a',1), ('b',6), ('a',3), ('c',7), ('a',9)]
reduced_rdd = rdd.reduceByKey(lambda x,y: x+y)
Output -> [('a',13), ('b',6), ('c',7)]

----------------------------------------------------------------------------------------------

Diff between groupByKey() and reduceByKey()

    groupByKey() -> complete shuffle happens to bring same key values together
    reduceByKey() -> aggregates first (local combine in each partition) and then shuffle
    Hence reduceByKey() is more efficient

'''