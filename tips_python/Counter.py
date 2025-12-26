'''

Counter()

-------------------------------------------------------------------------------------------------------

Counter() is a built-in class in Python (from collections module) 

    used to count the frequency of elements in a iterable

-------------------------------------------------------------------------------------------------------


Example_1:

    data = [1,2,2,3,3,3]

    c = Counter(data)

    print(c)     ->           #  Counter({3:3, 2:2, 1:1})


Example_2:

    text = "banana"

    c = Counter(text)

    print(c)    ->             # Counter({'a':3, 'b':1, 'n':2})

-------------------------------------------------------------------------------------------------------

In the c is similar to dictionary, we can access c how we do for dictionaries


Easy to check whether 2 strings are anagrams or not can be done using by Counter()

------------------------------------------------------------------------------------------------------
'''

from collections import Counter

var = 'abcdefbefzkrembax'

d = Counter(var)
print(d)
print(type(d))
print(d.get('e',0))


# Counter takes an iterable as input like string, list, tuple etc