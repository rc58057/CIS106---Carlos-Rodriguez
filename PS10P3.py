total_msrp = 0
total_sales_price = 0
while True:
  user_input = input("Would you like to continue? (Yes/No): ")
  if user_input.lower() != "yes":
      break
  make = input("Input Make: ")
  model = input("Input Model: ")
  elevcode = input("Input Vehicle Code (Y/N): ")
  msrp = float(input("Input MSRP: "))
  if make == "Honda" and model == "Accord":
      discount = .10
  elif make == "Toyota" and model == "Rav4":
      discount = .15
  elif elevcode == "Y":
      discount = .30
  else:
      discount = .05
  sales_price = msrp * (1 - discount)
  total_msrp += msrp
  total_sales_price += sales_price
print("Total MSRP:", total_msrp)
print("Total Sales Price:", total_sales_price)