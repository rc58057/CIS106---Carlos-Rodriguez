def calculate_total(quantity, price):
    total = quantity * price
    if total > 100000:
        total *= 0.9
    return total
extended_price = 0
while True:
    try:
        quantity = float(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        total = calculate_total(quantity, price)
        print(f"Quantity: {quantity}, Price: {price}, Total: {total}")
        extended_price += total
    except EOFError:
        break
print(f"Extended Price: {extended_price}")