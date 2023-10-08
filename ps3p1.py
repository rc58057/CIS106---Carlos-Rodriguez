#input phase
lname = input("Enter student last name")
midterm = float(input("Enter midtem score"))
final = float(input("Enter final exam score"))

#process phase
total = midterm + final

#output phase
print("Student:   ", lname)
print("Total points earned",total)