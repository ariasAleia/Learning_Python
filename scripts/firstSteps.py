print("Hello world. Here I go! Get ready :D") 

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

character_name = "John"
character_age = 35

print("There once was a man named " + character_name)
print("He was " + str(character_age) )
print("He liked the name " + character_name)
print("But he didn't like being " + str(character_age))


print("Sth with \"quotation")
print("Printing backslash\\")

#Some functions with strings:
phrase = "Aleja is learning to Code Better in Python"

#Changing to upper and lowercase
print(phrase.lower() + " [lowercase]")
print(phrase.upper() + " [uppercase]")
#Checking if it's uppercase
print(phrase.upper().isupper())

#Length function
print(len(phrase))

#Taking characters
#Last character is -1
print(phrase[-1])

#First character is 0
print(phrase[0])

#Get the index where a character (or group of characters) is located in our string. If it is found more than once, we will only get the first index where it appears.
print(phrase.index("ej"))
print(phrase.index("d"))
#If it's not found we will get an error
#print(phrase.index("k"))

#We can also replace
print(phrase.replace("Aleja", "Super Pro"))