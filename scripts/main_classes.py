from class_objects import Student

student1 = Student("Aleia", "Creative Programming", 5.0, False)
print(student1.name)
student2 = Student("Feliponcio", "Soccer analysis", 3.6, True)
print(student2.is_on_probation)

print(student1.in_honor_roll())
print(student2.in_honor_roll())