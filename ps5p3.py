#input
nb = int(input("Enter the number of books to order: "))
cpb = float(input("Enter the cost per book: "))

#process
ot = nb * cpb
sc = 0 if ot > 50 else 25
  
#output
print("The order total is: $", ot)
print("The shipping charge is: $", sc)