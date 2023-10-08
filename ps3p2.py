#input
sts = input("Enter Stock Ticker Symbol ")
nos = float(input("Enter Number of Share "))
cps = float(input("Enter Cost Per Share "))

#process
invested = nos * cps

#output
print("Stock ticker ", sts)
print("Your total amount invested was: ", invested)  
