'''

In python, the global keyword is used to modify variable inside a function, when variable is
defined outside the function


Example



x = 10


def update():
    global x
    x = x+5


update()
print(x)    -> 15


NOTE - x will be 15 everywhere not only inside update() function
'''