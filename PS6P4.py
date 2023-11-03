#input
num = int(input("Enter number of Tickets: "))
pr = 0
#process
if num < 25:
  pr = 50
if 10 < num < 24:
  pr = 60
if 9 < num < 5:
  pr = 70
if num < 5:
  pr = 75
total = num * pr
#output
print("Number of tickets: ", num)
print("Price per Ticket: ", pr)
print("Total Price: ", total)
