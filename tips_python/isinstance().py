'''


isinstance()



isinstance() in python is a built-in function used to check whether an object belongs to
specific class or tuple of classes

---------------------------------------------------------------------------------------

syntax  :  isinstance(object, classinfo)

object -> The variable or object we want to test

classinfo -> A class type or tuple of classes

----------------------------------------------------------------------------------------

Returns :

True / False

---------------------------------------------------------------------------------------

Examples

x = 5   print(isinstance(x, int))      # True
        print(isinstance(x, float))    # False


x = 3.14    print(isinstance(x, (int, float)))    # True


x = {"name": "Harsha", "age": 25}

print(isinstance(x, dict))    # True



'''