total = 0
tax = 0
def compute_total_and_tax(qty, unit_price):
    global total, tax
    total = qty * unit_price
    tax = 0.07 * total

def main():
    qty = float(input("Enter the quantity of the item: "))
    unit_price = float(input("Enter the unit price of the item: "))
    compute_total_and_tax(qty, unit_price)
    print("Total: ", total)
    print("Tax: ", tax)
main()