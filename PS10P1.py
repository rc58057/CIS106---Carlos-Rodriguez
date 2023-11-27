#input
while True:
  user_input = input("Do you want to enter sales data? (Yes/No): ")
  if user_input.lower() != "yes":
    break
  last_name = input("Enter last name: ")
  month = input("Enter month: ")
  sales = float(input("Enter sales: "))
  #process
if month in ("January", "February", "March"):
  for_per = 0.1
elif month in ("April", "May", "June"):
  for_per = 0.15
elif month in ("July", "August", "September"):
  for_per = 0.20
elif month in ("October", "November", "December"):
  for_per = 0.25
forecast = sales * for_per
  #output
print("Sales Forecast for", last_name, "in", month, "is", forecast)