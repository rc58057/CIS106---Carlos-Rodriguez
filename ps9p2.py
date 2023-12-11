def calculate_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    else:
        return hits / at_bats
player_count = int(input("Enter the number of players: "))
try:
    while True:
        last_name = input("Enter player's last name (or press Ctrl+Z to exit): ")
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at bats: "))
        average = calculate_batting_average(hits, at_bats)
        print(f"{last_name}'s batting average is {average}")
except KeyboardInterrupt:
    print("Exiting the program.")
print(f"Total number of players entered: {player_count}")

