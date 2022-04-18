import helper
import wordle
import random

if __name__ == "__main__": # Plays the game
    
    f = open("5Letter.txt")
    words = f.read().split("\n")
    solution = list(words[random.randint(0, 1378)].upper()) # Generate a random word for wordle
    attempts = 6

    # Generated from results of each round
    goodLetters=[]
    badLetters=[]
    first=""
    second=""
    third=""
    fourth=""
    fifth=""

    guess = "SALES" # First, most likely guess
    guesslist = []
    print("The solution for this round is " ,solution) # Debug line
    print()

    while attempts > 0: 
        print("Let's play round ",7-attempts)
        print("This round I will guess ",guess)
        result,flag = wordle.play(solution,guess) # Guesses the word

        if flag == 5: # Checks for win
            print("Congratulations you win")
            break

        for i in range(5): # Checks for character in position
            if result[i] == " " and i == 0:
                first = guess[i]
            
            elif result[i] == " " and i == 1:
                second = guess[i]
            
            elif result[i] == " " and i == 2:
                third = guess[i]
            
            elif result[i] == " " and i == 3:
                fourth = guess[i]
            
            elif result[i] == " " and i == 4:
                fifth = guess[i]

            elif result[i] == "'": # Checks good letters
                goodLetters.append(guess[i])

        for i in range(5): # Checks bad letters
            if result[i] == '"' and guess[i] not in goodLetters and guess[i] != first and guess[i] != second and guess[i] != third and guess[i] != fourth and guess[i] != fifth:
                badLetters.append(guess[i])
                
        attempts = attempts - 1
        guesslist.append(guess)
        print() 
        guess = helper.printTop(guesslist,goodLetters,badLetters,first,second,third,fourth,fifth) # Gets guess from helper function
        

    else: # If solver runs out of attempts
        print("You run out of attempts, you lose")
