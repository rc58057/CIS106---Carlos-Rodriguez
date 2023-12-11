def calculate_tuition(credit_hours, district_code):
    if district_code == "I":
        return 250 * credit_hours
    elif district_code == "O":
        return 550 * credit_hours
    else:
      return 0
tuition_total = 0
while True:
    try:
        student_last_name = input("Enter student last name: ")
        if student_last_name == "":
            break
        credit_hours = int(input("Enter credit hours: "))
        district_code = input("Enter district code (I for In-district, O for Out-of-district): ")
        tuition_owed = calculate_tuition(credit_hours, district_code)
        tuition_total += tuition_owed
        print(f"Student Name: {student_last_name}, Tuition Owed: ${tuition_owed}")
    except ValueError:
        print("Invalid input. Please enter a valid number for credit hours.")
print(f"Total Tuition Owed: ${tuition_total}")