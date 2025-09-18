nested_list = [[1, 2], [3, 4, 5], [6], 7]

flat_list=[]

for x in nested_list:
    if isinstance(x, list):
        for y in x:
            flat_list.append(y)
    else:
        flat_list.append(x)
    
print(flat_list)

# isinstance(variable, datatype) returns True or False