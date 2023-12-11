def main():
  with open('students.txt', 'w') as file:
      num_students = int(input("Enter the number of students: "))
      total_tuition = 0
      for _ in range(num_students):
          name = input("Enter student last name: ")
          district_code = input("Enter district code (I or O): ")
          credits_taken = int(input("Enter number of credits taken: "))
          cost_per_credit = 250.0 if district_code.upper() == 'I' else 500.0
          tuition_owed = credits_taken * cost_per_credit
          total_tuition += tuition_owed
          file.write(f"{name}, {credits_taken}, {tuition_owed}\n")
      print(f"Total tuition owed: {total_tuition}")
      print(f"Number of students: {num_students}")
if __name__ == "__main__":
  main()