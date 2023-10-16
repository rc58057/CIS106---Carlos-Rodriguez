#input 
tom = input("Enter total of meal ")
tip = float(input( "Enter tip percentage "))
#process
twt = float(tom) * float(tip) / 100
total = float(tom) + float(twt)
#output
print("Total:          ",tom)
print("The tip is:     ",twt)
print("Total with tip: ",total)