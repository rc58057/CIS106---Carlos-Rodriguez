total_market_value = 0
total_assessed_value = 0
while True:
  county = input("Enter the name of the county: ")
  Mrktvalue = float(input("Enter the market value: "))

  if county == "cook":
    asvalper = 0.9
  elif county == "DuPage":
    asvalper = 0.80
  elif county == "McHenry":
    asvalper = 0.75
  elif county == "Kane":
    asvalper = 0.60
  else:
    asvalper = 0.70

  asval = asvalper * Mrktvalue
  total_market_value += Mrktvalue
  total_assessed_value += asval
  print("The assessed value is:", asval)
  user_input = input("Would you like to continue? (Yes/No): ")
  if user_input.lower() != "yes":
      break
print("Total market value:", total_market_value)
print("Total assessed value:", total_assessed_value)