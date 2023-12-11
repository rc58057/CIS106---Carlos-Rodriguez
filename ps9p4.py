def determine_pay_rate(job_code):
    if job_code == "L":
        return 25
    elif job_code == "A":
        return 30
    elif job_code == "J":
        return 50
employee_data = []
total_gross_pay = 0
while True:
    last_name = input("Enter last name: ")
    job_code = input("Enter job code: ")
    hours_worked = float(input("Enter hours worked: "))

    pay_rate = determine_pay_rate(job_code)

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        gross_pay = 40 * pay_rate + overtime_hours * (1.5 * pay_rate)
    else:
        gross_pay = hours_worked * pay_rate

    total_gross_pay += gross_pay

    print("Last name:", last_name)
    print("Gross pay:", gross_pay)

    employee_data.append((last_name, gross_pay))

    try:
        ctrl_z = input()  # Windows command to stop is Ctrl-Z
    except:
        break
print("Total gross pay:", total_gross_pay)