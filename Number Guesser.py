import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()
else: 
    print("Please enter a number next time.")
    quit()



Random_N = random.randrange(0, top_of_range)

Guesses = 0

while True: 
    Guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == Random_N:
        print("You got it right")
        
        break
    else:
        print("That is incorrect")
    

plural = "time" if Guesses == 1 else "times"

print("It took",str(Guesses), plural, "to get it right")  

