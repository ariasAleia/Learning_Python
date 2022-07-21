# If both files are in the same folder, then we just need the name of the file
# The second parameter specifies if we want to read or modify or write the file
# r means that we only want to read from it
# w is that we want to write in the file, change it
# a means append, we can add new info to the file
# r+ -> means read and write
employee_file = open("scripts\employees.txt", "r")

#This returns a True if we can read it. (if we have "r": True, if we have "w", for example: False)
print(employee_file.readable())

#To read lines in the file but it moves the cursor so that the next time when we want to read it won't
#read the whole file. Better not use it

# print(employee_file.readline())
# print(employee_file.readline())

#To get all the info from the file but it moves the cursor so that the next time when we want to read it won't
#read the whole file. Better not use it:

# print(employee_file.read())

#Sth that we can do that is actually faaar better is:
list_of_employees = employee_file.readlines()

#But  again!!! it moves the cursor so that the next time when we want to read it won't
#read the whole file. Better not use it more than once. It's better to save it in a variable

#With that we have all the info saved in a list

#And now we can do magic!

for employee in list_of_employees:
    print(employee)
    
#Or just take one specific value:
print("Just one employee: " + list_of_employees[2])


#Remember to close the file!
employee_file.close()
