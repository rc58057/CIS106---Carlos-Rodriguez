#input
qoi = int(input("Enter Quantity of item: "))

#process
up = 3 if qoi >= 1000 else 5
ep = qoi * up
tax = round(0.07 * ep, 2)
total = round(ep * tax, 2)
  
#output
print("Quantity: ", qoi)
print("Unit price: ", up)
print("Extended price:", ep)
print("Tax:", tax)
print("Total:", total)
