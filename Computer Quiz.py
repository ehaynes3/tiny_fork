print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay Lets Play")
Score = 0

answer = input(" What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    Score += 1
else: print("Sorry that is not correct.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    Score += 1
else: print("Sorry that is not correct.")

answer = input(" What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    Score += 1
else: print("Sorry that is not correct.")

answer = input(" What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    Score += 1
else: print("Sorry that is not correct.")
print("You got " + str(Score) + " questions correct")
print ("Your score is " + str(Score/4*100))