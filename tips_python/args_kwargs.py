'''

*args  -  Variable length positional arguments

**kwargs  -  Variable length keyword arguments

-----------------------------------------------------------------------------------------------

Example

def example(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

example(1, 2, 3, 4, 5, x=10, y=20)

--------------------------------------------------------------------------------------------------

a -> 1
b -> 2
args -> (3,4,5)
kwargs -> {'x'=10, 'y'=20}


args will be TUPLE by default
kwargs will be DICTIONARY by default


'''