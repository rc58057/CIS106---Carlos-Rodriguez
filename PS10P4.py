user_input = input("Would you like to continue? (Yes/No): ")
if user_input.lower() != "yes":
    break
lastname = input("Enter last name: ")
mfdt = float(input("Enter miles from downtown: "))
if mfdt < 30:
    tixprice = 12
elif 29 < mfdt < 20:
    tixprice = 10
elif 19 < mfdt < 10:
    tixprice = 8
else:
    tixprice = 5
print("The ticket price is: $" + str(tixprice))