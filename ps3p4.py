#input
mk = input("Enter Make: ")
mdl = input("Enter Model: ")
msrp = float(input("Enter MSPR: "))
discnt = float(input("Enter Discount: "))
#process
ammoff = msrp * discnt
dispri = msrp - ammoff
#output
print("Make: ", mk)
print("Model: ", mdl)
print("MSRP: ", msrp)
print("Discount: ", discnt)
print("Amount off: ", ammoff)
print("Discounted Price: ", dispri)