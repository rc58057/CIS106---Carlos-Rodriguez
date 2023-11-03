#input
part_num = input("Enter part number: ")
qty = int(input("Enter quantity: "))
#process
if part_num == "10" or part_num == "55":
  unit_cost = 1.00
elif part_num == "99":
  unit_cost = 2.00
elif part_num == "80" or part_num == "70":
  unit_cost = 3.00
else:
  unit_cost = 5.00

total = qty * unit_cost
#output
print("Part number:", part_num)
print("Unit cost:", unit_cost)
print("Total:", total)