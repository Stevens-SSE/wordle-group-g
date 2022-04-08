import random

class Wordle:

    solution = []
    attemptList = []
    attempts = 6
    wordList = []

    def __init__(self):
        f = open("5Letter.txt")
        words = f.read().split("\n")
        self.wordList = words
        self.solution = list(words[random.randint(0, 1378)].upper())

    def __str__ (self):
        attemptsMade = ",".join(self.attemptList)
        return 'Solution is ' + "".join(self.solution) + ' number of attempts remaining is ' + str(self.attempts) + ' and words attempted till now are ' + attemptsMade
    
    def intro(self):
        print()
        print("Welcome to wordle")
        print()
        print("Correct letters in correct positions will have a ' ' under them, correct letters in incorrect positions will have a '\'' under them and incorrect letters will have '\"' under them.")
        print("You will have 6 guesses.")
        print()

    def loss(self):
        print()
        print("Sorry you have run out of attempts. You lose, the word was "+ "".join(self.solution))

    def input(self):
        while True:
            temp = input()
            temp = list(temp.upper())
            if len(temp) != 5:
                print()
                return ("Word length is not 5")
            elif "".join(temp) in self.attemptList:
                print()
                return ("Word has already been tried")
            elif not "".join(temp).isalpha():
                print()
                return ("Word has non alphabetic characters")
            elif "".join(temp) not in self.wordList:
                print()
                return ("Word doesn't exist")
            else:
                self.attemptList.append("".join(temp))
                return temp

    def checkWord(self,currentAttempt):

        flag = 0 # Tracks number of letters rightly guessed in the correct position on each attempt to check if user has one
        result = ["","","","",""] # Assigns " ",""" or "'" depending on correct and incorrect letters and positions
        search = ["0","0","0","0","0"] # Used to check if a letter has been used, so same letter doesn't give 2 positive outputs.
        pos = 0 # Used to track the letter that is being used in the actual word to create result

        for i in range(5): # Checking for correct letters in correct positions first, to ensure highest priority
            if(currentAttempt[i] == self.solution[i]):
                flag = flag + 1
                result[i] = (" ")
                search[i] = 1

        for i in range(5): # Checking for correct letters in incorrect position and lastly incorrect letters
            if(currentAttempt[i] in self.solution and result[i] == ""):
                pos = "".join(self.solution).find(currentAttempt[i])
                if(search[pos] == 1):
                    result[i] = ("\"")
                else:
                    result[i] = ("'")
                    search[pos] = 1
            elif result[i] == "":
                result[i] = ("\"")
        
        return (result,flag)
    
    def win(self):
        print()
        print("Congratulations you have guessed the right word!")
        print()


def runWordle(solution,tests):
    w = Wordle()
    w.solution = solution
    w.intro()
    print(w.__str__())
    while w.attempts > 0:
        print()
        print("Please make your "+ str(7 - w.attempts) + " guess")
        currentAttempt = tests[6-w.attempts]
        if currentAttempt == "Word length is not 5":
            return "Size error"
        if currentAttempt == "Word has already been tried":
            return "Word has already been tried"
        if currentAttempt == "Word has non alphabetic characters":
            return "Not alphabetic"
        if currentAttempt == "Word doesn't exist":
            return "Not a dictionary word"
        
        result,flag = w.checkWord(currentAttempt)

        if flag == 5:
            w.win()
            return "WIN on " + str(w.attempts)

        for i in range(5):
            print(currentAttempt[i],end = "")
        print()

        for i in range(5):
            print(result[i], end = "")
        print()

        w.attempts -= 1
    else:
        w.loss()
        return "LOSS"

if __name__ == "__main__":
    print("Please run via tests.py. This file is only for testing")
    