#input
pps = int(input("Enter Price Per Share "))
csp = int(input("Enter Stock Price "))
qos = int(input("Enter Quantity of Stocks "))
#process
vos = csp + pps * qos
#output
print("value of the stock is ", vos)