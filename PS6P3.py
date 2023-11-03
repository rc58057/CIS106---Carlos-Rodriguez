#input
paoc = int(input("Enter principle amount of a CD: "))
yom = int(input("Enter year to maturity of CD: "))
#process
if yom < 100000 and yom == 5:
  rate = .06
if 100000 < paoc < 50000 and yom == 10:
  rate = .05
if 100000 < paoc < 50000 and yom == 5:
  rate = .04
if paoc < 50000:
  rate: .02
fyi = paoc * rate
#output
print("Principle : " , paoc)
print("Interest rate" , rate)
print("Interest amount for first year: " , fyi)