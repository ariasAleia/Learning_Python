friends = ["Feliponcio", "Dan", "Cristian", "Sebas"]
print(friends)
friends[0] = "F"
print(friends[-1])
print(friends[0])
print(friends[-2])
print(friends[1])

print(friends[1:3])

lucky_numbers = [4, 8, 15, 16, 23, 42]
print(lucky_numbers)
friends[0] = "Feliponcio"
friends.extend(lucky_numbers)
print(friends)

lucky_numbers.append(9)
print(lucky_numbers)

lucky_numbers.insert(2, 17)
print(lucky_numbers)

lucky_numbers.remove(15)
print(lucky_numbers)

lucky_numbers.pop()
print(lucky_numbers)

lucky_numbers.pop(2)
print(lucky_numbers)

print(friends.index("Dan"))

friends[4] = "New friend"
friends[6] = "New friend"
print(friends.count("New friend"))

friends.clear()
print(friends)
friends.append("Feliponcio")
friends.append("Dan")
friends.append("Cristian")
print(friends)
friends.sort()
print(friends)

print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

#Jap... We cannot copy that easy. It would modify both lists. They both point to the same list
other_friends = friends
print(other_friends)
other_friends.append("Sam")
print(other_friends)
print(friends)



# If we want to copy we gotta use the function copy to create another list that has the same content but that is independent
other_friends = friends.copy()
print(other_friends)
other_friends.append("Sam2")
print(other_friends)
print(friends)