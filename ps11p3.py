def calculate_commission_and_target():
    last_name = input("Enter salesperson's last name: ")
    sales = float(input("Enter the sales amount: "))
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    next_year_target = sales * 0.05
    print(f"Salesperson: {last_name}")
    print(f"Commission: {commission}")
    print(f"Next year's target: {next_year_target}")
calculate_commission_and_target()