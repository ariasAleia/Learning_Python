# Here we will basically open a file and append info to it
# That means that we will add info at the end of the file
print("If we want to print sth but it's extremely large we can "
      "simply split it like this")
employee_file = open("scripts\employees.txt", "a")
employee_file.write("\nLuck - Catalyzer")
#And taraaaaaaaaaaaaaaan we will see in the file that sth new was added at the end
#But be careful!!! If you run the code multiple times, it will add the new line many times and it
#can get messy
employee_file.close()