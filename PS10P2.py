#input
while True:
    user_input = input("Would you like to continue? (Yes/No): ")
    if user_input.lower() != "yes":
        break
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    height = float(input("Enter Height: "))
    squared_feet = (2 * length * width) + (2 * length * height) + (2 * width * height)
    paint = squared_feet / 50
    print(f"You will need {paint:.2f} gallons of paint to cover {squared_feet} square feet of wall space")
