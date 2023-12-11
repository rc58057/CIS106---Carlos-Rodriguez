bonus_info = []
while True:
    last_name = input("Enter last name: ")
    salary = float(input("Enter salary: "))
    if salary >= 100000:
        bonus_rate = 0.20
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10
    bonus = salary * bonus_rate
    bonus_info.append((last_name, salary, bonus))
    option = input("Do you want to enter another employee (yes/no)? ")
    if option.lower() != "yes":
        break
total_bonus = sum(bonus_info[i][2] for i in range(len(bonus_info)))
with open("employee_info.txt", "w") as file:
    for info in bonus_info:
        file.write(f"{info[0]}: {info[1]}, Bonus: {info[2]}\n")
print(f"Total bonus paid out: {total_bonus}")