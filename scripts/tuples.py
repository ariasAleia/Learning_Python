coordinates = (4, 5)
print(coordinates)
print(coordinates[1])

#If we try to modify a value of the tuple it will give us an error
#coordinates[0] = 2

#Something cool: A list of tuples

#We can do this...
list = [(8,9), (7,8), (6,7)]
print(list)
list[0] = 4
print(list)

#But not this:
#list[1][1] = 4
#print(list)

#And if we do a tuple of lists?
tuple_of_lists = ([4,5], [5,6])
print(tuple_of_lists)

#We can modify the list in the tuple
tuple_of_lists[0][1] = 3
print(tuple_of_lists)

#But we cannot modify the tuple itself

tuple_of_lists[0] = [4,3]
print(tuple_of_lists)