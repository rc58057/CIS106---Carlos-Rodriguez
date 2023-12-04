def compute_average_and_total(last_name, score1, score2, score3):
  total_points = score1 + score2 + score3
  average_score = total_points / 3
  return total_points, average_score
def display_student_info(last_name, total_points, average_score):
  print(f"Student last name: {last_name}")
  print(f"Total points: {total_points}")
  print(f"Average exam score: {average_score}")
last_name = input("Enter the student's last name: ")
score1 = float(input("Enter exam score 1: "))
score2 = float(input("Enter exam score 2: "))
score3 = float(input("Enter exam score 3: "))
total, average = compute_average_and_total(last_name, score1, score2, score3)
display_student_info(last_name, total, average)

