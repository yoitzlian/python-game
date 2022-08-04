import random 

def guessing_game():
    while True: 
        num = random.randint(1,101)
        guesses = 0
        guess = int(input("What number you think will be? "))
        if (guess < 1) or (guess > 100):
            print("Invalid input! ")
        elif (guess < num):
            print("Too low ,Try again. ")
        elif (guess > num):
            print("Too High, Try again. ")

            num_guesses = num_guesses + 1
        else:
            print("You were wrong :(. The Number was " + str(guess))
            break
    print("You guessed right " + str(num_guesses) + " times")
    #I hope it works :)
