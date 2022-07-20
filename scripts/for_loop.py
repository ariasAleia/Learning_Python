for letter in "Aleia is coding":
    print(letter)
    
friends = ["You", "Me", "We both"]
for friend in friends:
    print(friend)
    
for i in range(10):
    print(i)
#Output: 0 1 2 3 4 5 6 7 8 9
for i in range(3, 10):
    print(i)
#Output: 3 4 5 6 7 8 9

#And in a not so pythonic way we can also iterate through a list:
for index in range(len(friends)):
    print(friends[index])