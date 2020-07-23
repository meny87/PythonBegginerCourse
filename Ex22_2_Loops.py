# Create a guess game with the names of the colors. I neeAt each round pick a random color from the list and let the user guess it. 
# When he does it, ask him if he wants to play again. Keep playing until the user types "no"

import random
colors = ["Blue", "Yellow", "Red", "Purple", "Green", "Brown", "Gray", "Black", "White"]

keepPLaying = True
randomIndex = random.randint(0,len(colors)-1)
randomColor = colors[randomIndex]
pickedColor = ""
currRound = 1

print ("List of Colors: ", colors)

while keepPLaying:
    print (" ------  Round " + str(currRound) + " ------ ")
    while pickedColor != randomColor:
        pickedColor = input("I've chosen a name of a color from the above list, try to guess it (Type 'no' to stop playing): ")
        if pickedColor.lower() == "no":
            print("Thanks for playing! See you next time.")
            keepPLaying = False
            break
        elif pickedColor.lower() == randomColor.lower():
            print("Yay!!! You guessed the color ", randomColor)
            randomIndex = random.randint(0,len(colors)-1)
            randomColor = colors[randomIndex]
            print (randomColor)
            currRound += 1
            break
        else:
            print("Keep Trying!")