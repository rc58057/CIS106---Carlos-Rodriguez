def compute_average(scores):
    return sum(scores) / len(scores)
ui = input("Do you want to continue? (Yes/No) ")
count = 0
while ui.lower() == "yes":
    last_name = input("Enter your last name: ")
    exam_scores = []
    exam_scores.append(float(input("Enter your first exam score: ")))
    exam_scores.append(float(input("Enter your second exam score: ")))
    avg_score = compute_average(exam_scores)
    print("Last name:", last_name)
    print("Average score:", avg_score)
    count += 1
    ui = input("Do you want to continue? (Yes/No) ")
print("Number of students entered:", count)