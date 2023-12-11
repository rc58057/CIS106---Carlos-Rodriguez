def main():
    total_interest = 0
    principle = float(input("Enter the principle amount: "))
    interest_rate = float(input("Enter the interest rate: "))

    for year in range(1, 6):
        interest = principle * interest_rate
        ending_balance = principle + interest
        total_interest += interest
        print(f"Year: {year}, Beginning Balance: {principle}, Ending Balance: {ending_balance}")
        principle = ending_balance
    print(f"Accumulated Interest for 5 years: {total_interest}")
main()