# w stands for write.
# If the file doesn't exist, then we will create if with this. But!!! if the file exists we will totally overwrite it and 
# lose all the data we had there. So! Take care when writing in files
employee_file = open("scripts\employees1.txt", "w")
print(employee_file.writable())
employee_file.write("This is the line that will overwrite whatever "
                    "we may find in the file. This is dangerous!")
employee_file.close()