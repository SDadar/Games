import random
randNumber = random.randint(1, 10)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("HighScore.txt", "r") as f:
    HighScore = int(f.read())

if(guesses<HighScore):
    print("You have just broken the high score!")
    with open("HighScore.txt", "w") as f:
        f.write(str(guesses))
