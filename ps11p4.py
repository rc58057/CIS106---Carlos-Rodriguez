def calculate_average_score(scores):
  return sum(scores) / len(scores)
def calculate_average_score_with_handicap(scores, handicap):
  return (sum(scores) + handicap) / len(scores)
def main():
  last_name = input("Enter bowler's last name: ")
  game1 = float(input("Enter game 1 score: "))
  game2 = float(input("Enter game 2 score: "))
  game3 = float(input("Enter game 3 score: "))
  handicap = float(input("Enter handicap: "))
  scores = [game1, game2, game3]
  avg_score = calculate_average_score(scores)
  avg_score_handicap = calculate_average_score_with_handicap(scores, handicap)
  print("Last Name:", last_name)
  print("Average Score:", avg_score)
  print("Average Score with Handicap:", avg_score_handicap)
if __name__ == "__main__":
  main()