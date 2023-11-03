#input
elm = input("Enter Employee last name: ")
sal = int(input("Enter Salary: $"))
jbl = int(input("Enter Job level: "))
bonus = 0
#process
if jbl > 10:
  bonus = sal * .25
if 9 > jbl > 5:
  bonus = sal * .2
if jbl > 5:
  bonus = sal * .1
#output
print("Employee:", elm)
print("Bonus: $", bonus)
