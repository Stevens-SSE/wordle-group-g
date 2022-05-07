
from HW_08_Yash_Gilda_Wordle_Helper import Helper as helper
import HW03_Yash_Gilda_ui as ui
import HW03_Yash_Gilda_wordle as wordle
import HW_12_Yash_Gilda_DB as db
import random



def solver(dbLogger):    
    f = open("word_list.txt")
    words = f.read().split("\n")
    solution = list(words[random.randint(0, 1378)].lower()) # Generate a random word for wordle
    attempts = 6
    
    # Generated from results of each round
    goodLetters=[]
    badLetters=[]
    first=""
    second=""
    third=""
    fourth=""
    fifth=""

    guess = "sales" # First, most likely guess
    guesslist = []
    sol = ""
    for i in solution:
        sol+=i
    print("The wordle is: " ,sol) # Debug line
    print()
    dbLogger.insert_to_game(sol)
    while attempts > 0: 
        print("Attempt Number: ",7-attempts)
        print("System Guess: ",guess)
        result,flag = wordle.play(sol,guess) # Guesses the word

        if flag == 5: # Checks for win
            print("Congratulations you win!!")
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
        dbLogger.insert_to_statistics(True, attempts)
        guesslist.append(guess)
        print() 
        guess = helper.printTop(guesslist,goodLetters,badLetters,first,second,third,fourth,fifth) # Gets guess from helper function
        if guess == None:
            print("Failed to solve the Wordle \n")
            dbLogger.insert_to_statistics(False, attempts)
            break

    else: # If solver runs out of attempts
        print("Out of attempts!! You lose!!")



dbLogger = db.DbLogger()
for i in range(1000):
    print(f"Game Number: {i}")
    solver(dbLogger)
dbLogger.report_analysis("2022-01-01",
                        "2022-12-12")
dbLogger.close()       