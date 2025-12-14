'''

.get()

--------------------------------------------------------------------------------------------------------

.get() method in python is most commonly used with Dictionaries.

It's a safe way to access a key without causing an error if the key doesn't exist.

--------------------------------------------------------------------------------------------------------

syntax :   dict_var.get(key, default)

--------------------------------------------------------------------------------------------------------


without  .get()

person = {'name': "Harsha", 'age': 25}


print(person['name'])    # works fine

print(person['city'])    # KeyError: 'city'

-------------------------------------------------------------------------------------------------------


using .get()


print(person.get('name'))       # Harsha
print(person.get('city'))       # None (no error)

print(person.get('city',  'Bangalore'))      # Bangalore (default value)



.get() avoids a KeyError when the key doesn't exist

-------------------------------------------------------------------------------------------------------


Nested access


data = {'user': {'id':101, 'role': 'admin'}}

role = data.get('user', {}).get('role', 'guest')


print(role)   # admin
--------------------------------------------------------------------------------------------------------
'''