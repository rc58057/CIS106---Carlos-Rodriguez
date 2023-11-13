loop_control = input("Do you want to continue? (Yes/No): ")
while loop_control == "Yes":
  quantity = float(input("Enter quantity: "))
  price = float(input("Enter price: "))
  extended_price = quantity * price
  discount = 0.25 if extended_price > 10000.0 else 0.1
  discount_amount = extended_price * discount
  total = extended_price - discount_amount
  print(f"Extended Price: {extended_price}")
  print(f"Discount Amount: {discount_amount}")
  print(f"Total: {total}")
  loop_control = input("Do you want to continue? (Yes/No): ")