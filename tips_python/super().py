# super() is used to call functions in parent class


# below Person is parent and Employee is child


class Person:
    def __init__(self, name):
        print("Person __init__ called")
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        print("Employee __init__ called")
        super().__init__(name)
        self.emp_id = emp_id

emp = Employee("Harsha", 101)

print(emp.name)
print(emp.emp_id)


# self.name == emp.name