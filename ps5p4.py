#input
nm = input("Name of Appliance: ")
c = float(input("Cost: $"))
 #process
wc = c * 0.1 if c > 1000 else c * 0.05
tc = c + wc
#output
print("Name of Appliance: ", nm)
print("Cost: $", c)
print("Warranty Cost: $", wc)
print("Total Cost: $", tc)
  