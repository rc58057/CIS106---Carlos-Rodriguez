#input
lm = input("Enter Last name: ")
dp = int(input("Enter number of dependants: "))
gi = float(input("Enter gross income: "))
#process
agi = gi - dp
tax_rate = 0.2 if agi > 50000 else 0.1

it = agi * tax_rate

if it < 0:
  it = 100
#output
print("Last Name: ", lm)
print("Gross Income: ", gi)
print("Number of Dependants: ", dp)
print("Adjusted gross income: ", agi)
print("Income tax: ", it)
