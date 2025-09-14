from functools import reduce
List = [24,8,13,0,73,69,15,32]

try :

    lambda_example = lambda x,y : x+y
    print(lambda_example(2,10))

    map_result = [map(lambda x : x**2, List)]
    print(f"map example answer : {map_result}")

    filter_result = [filter(lambda x : x%2==0, List)]
    print(f"filter example answer : {filter_result}")

    reduce_result = [reduce(lambda x,y : x+y, List)]
    print(f"reduce example answer : {reduce_result}")

except Exception as e:
    raise