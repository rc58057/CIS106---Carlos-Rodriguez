keep_going = True
while keep_going:
  response = input("Do you want to continue? (Yes/No): ")

  if response.lower() == "yes":
    employee_count = 0
    total_gross_pay = 0

    while True:
      last_name = input("Enter employee last name: ")
      hours_worked = float(input("Enter hours worked: "))
      rate_of_pay = float(input("Enter rate of pay: "))

      if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (rate_of_pay * 1.5)
        gross_pay = (40 * rate_of_pay) + overtime_pay
      else:
        gross_pay = hours_worked * rate_of_pay

      print("Last name:", last_name)
      print("Gross pay:", gross_pay)

      employee_count += 1
      total_gross_pay += gross_pay

      response = input("Do you want to enter data for another employee? (Yes/No): ")
      if response.lower() != "yes":
        break

    print("Total gross pay:", total_gross_pay)
    print("Employee count:", employee_count)
    print("Average pay:", total_gross_pay / employee_count)

    continue_loop = input("Do you want to do this loop again? (Yes/No): ")
    if continue_loop.lower() != "yes":
      keep_going = False
  else:
    keep_going = False