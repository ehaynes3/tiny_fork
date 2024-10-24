import random
user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        #print("That is not a valid option")
        continue

    rand_num = random.randint(0,2)
    # Rock = 0, paper = 1, Sissors = 2
    computer_pick = options[rand_num]
    print("The computer picked",computer_pick + "." )

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
    else:
        print("You Lost.")
        comp_wins += 1


print("You won", user_wins,"times.")
print("The Computer won", comp_wins,"times.")

print("Goodbye!")