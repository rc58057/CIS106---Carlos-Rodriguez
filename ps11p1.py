def calculate_discount_and_discounted_price(quantity, price, discount_rate):
  discount_amount = price * discount_rate
  discounted_price = price - discount_amount
  return discount_amount, discounted_price
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate: "))
discount_amount, discounted_price = calculate_discount_and_discounted_price(quantity, price, discount_rate)
print("Quantity:", quantity)
print("Price:", price)
print("Discount Amount:", discount_amount)
print("Discounted Price:", discounted_price)