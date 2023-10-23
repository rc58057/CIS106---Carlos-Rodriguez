#input
item = input("Enter Item: ")
qty = int(input("Enter Quantity: "))

#process
up = 10 if item == "A" else 20
ep = qty * up

#output
print("Item: ", item)
print("Unit Price: $", up)
print("Extended Price: $", ep)