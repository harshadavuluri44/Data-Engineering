'''

In Python, __repr__ is a special method that defines what the object is about in string format,
mainly used by developers for debugging

------------------------------------------------------------------------------------------------------


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"The class Point({self.x},{self.y})"


p = Point(3,4)
print(p)  ->   this calls __repr__

Output :- The class Point(3,4)

-----------------------------------------------------------------------------------------------------

If we have both __str()__ and __repr()__ in a class

    The preference goes to __str()__ when a object is printed


Example

Class Example:
    def __repr__(self):
        return 'repr-version'

    def __str__(self):
        return 'str-version'


e = Example()


print(e)  ->     str-version

In this to execute __repr__   use print(repr(e))


'''