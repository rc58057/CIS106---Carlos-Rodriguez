#input
qty = int(input("Enter Quantity of Widgets: "))
#process
if qty > 10000:
  price = 10
elif qty > 5000:
  price = 20
else:
  price = 30

ep = qty * price
tax = round(ep * .07, 3)
total = round(ep * tax, 3)

#output
print("Extended Price: $", ep)
print("Tax: $", tax)
print("Total: $", total)