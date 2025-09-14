'''

mapPartitions(), groupByKey(), reduceByKey() are RDD operations only, they are not availanle in
DataFrame API
-----------------------------------------------------------------------------------------------
3. map() - Transformation

* Applies a function to each element of RDD/ DataFrame
* Output : one element per input element (1-to-1 mapping)

syntax :- rdd.map(func)

let's assume rdd is [1,2,3]

mapped_rdd = rdd.map(lambda x:[x,x*2])

[[1,1],[2,4],[3,6]]
----------------------------------------------------------------------------------------------
4. flatMap()

Works same as map, Applies a function to each element, but function return multiple elements or none
* output :- flattened list of results

rdd = ['hello world', 'spark rdd']

flatted_rdd = rdd.flatMap(lambda line: line.split(" "))

flatted_rdd = ['hello', 'world', 'spark', 'rdd']

DIFF B/W MAP() AND FLATMAP() IN SPARK

1. Output per input - exactly 1 in map()
   0 or more in flatmap()

2. Data Structure - map() keeps nested structure (ex: list of lists)
                    flatMap() flattens results into single sequence

3. Use Case - map() Transforms each element
              flatMap() split/ explode elements

------------------------------------------------------------------------------------------

1. mapPartitions() - Applies function to each partition independently.

syntax :- rdd.mapPartitions(func)

Example 
def func(iterator):
    result=[]
    for x in iterator:
        result.append(x*2)
    return result

mapped_rdd = rdd.mapPartitions(func)
-------------------------------------------------------------------------------------------------

2. groupByKey() :- groups all values for each key together 

    similar to groupBy in dataframe

example : rdd = [('a',1), ('b',6), ('a',3), ('c',7), ('a',9)]

grouped_rdd = rdd.groupByKey()

grouped_rdd = [('a',[1,3,9]), ('b',6), ('c',7)]
-------------------------------------------------------------------------------------------


'''