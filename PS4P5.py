#input
fc = float(input("Enter the Fixed costs: "))
ppu = float(input("Enter Price per Unit: "))
cpu = float(input("Enter Cost per Unit: "))
#process
brp = fc / ppu * cpu
#output
print("The Breaking Point is: ",brp)