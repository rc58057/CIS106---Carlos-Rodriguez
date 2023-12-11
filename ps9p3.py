def compute_mpg(miles, gallons):
    return miles / gallons
trips = 0
while True:
    try:
        destination_city = input("Enter destination city: ")
        miles_traveled = float(input("Enter miles traveled: "))
        gallons_used = float(input("Enter gallons used: "))
        mpg = compute_mpg(miles_traveled, gallons_used)
        trips += 1
        print(f"Destination City: {destination_city}, Miles: {miles_traveled}, MPG: {mpg}")
    except EOFError:
        break
print(f"Number of entries: {trips}")