orders = []
sum_extended_price = 0
while True:
    item = input("Enter item name or 'done' to finish: ")
    if item.lower() == 'done':
        break
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    extended_price = quantity * price
    sum_extended_price += extended_price
    orders.append((item, quantity, price, extended_price))
for order in orders:
    print(f"Item: {order[0]}, Quantity: {order[1]}, Price: {order[2]}, Extended Price: {order[3]}")
count_orders = len(orders)
average_order = sum_extended_price / count_orders
print(f"Sum of all extended prices: {sum_extended_price}")
print(f"Number of orders: {count_orders}")
print(f"Average order: {average_order}")
with open('orders.txt', 'w') as file:
    file.write("Item | Quantity | Price | Extended Price\n")
    for order in orders:
        file.write(f"{order[0]} | {order[1]} | {order[2]} | {order[3]}\n")