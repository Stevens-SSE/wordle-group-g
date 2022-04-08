import pandas as pd

class Node: # Node class
  # constructor
  def __init__(self, data, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print first 50 method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
  def print50(self):
    current = self.head
    count = 0
    while(current and count < 50):
      print(current.data)
      count = count + 1
      current = current.next


if __name__ == "__main__": # Runs if user uses helper
    print("Hello! This is the wordle helper.")
    print()
    print("Please enter the good letters or enter for no known good letters")
    while True: # Takes good letters
        good = input()
        if len(good)>5:
            print("You cannot have more than 5 good letters")
            continue
        if not (good.isalpha() or good == ""):
            print("You entered non alphabetic character")
            continue
        break
    good = good.upper()
    good = list(set(list(good)))
    
    print("Please enter bad letters or enter for no known bad letters")
    while True: # Takes bad letters
        bad = input()
        if not (bad.isalpha() or bad == ""):
            print("You entered non alphabetic character")
            continue
        break
    bad = bad.upper()
    bad = list(set(list(bad)))

    # Takes all 5 letters if known
    print("Please enter character at position 1, enter if it is not known")    
    while True:
        first = input()
        if len(first) > 1:
            print("Please enter a single character")
            continue
        if not (first.isalpha() or first == ""):
            print("Please enter an alphabet or space")
        break
    first = first.upper()

    print("Please enter character at position 2, enter if it is not known")    
    while True:
        second = input()
        if len(second) > 1:
            print("Please enter a single character")
            continue
        if not (second.isalpha() or second == ""):
            print("Please enter an alphabet or space")
        break
    second = second.upper()

    print("Please enter character at position 3, enter if it is not known")    
    while True:
        third = input()
        if len(third) > 1:
            print("Please enter a single character")
            continue
        if not (third.isalpha() or third == ""):
            print("Please enter an alphabet or space")
        break
    third = third.upper()

    print("Please enter character at position 4, enter if it is not known")    
    while True:
        fourth = input()
        if len(fourth) > 1:
            print("Please enter a single character")
            continue
        if not (fourth.isalpha() or fourth == ""):
            print("Please enter an alphabet or space")
        break
    fourth = fourth.upper()

    print("Please enter character at position 5, enter if it is not known")    
    while True:
        fifth = input()
        if len(fifth) > 1:
            print("Please enter a single character")
            continue
        if not (fifth.isalpha() or fifth == ""):
            print("Please enter an alphabet or space")
        break
    fifth = fifth.upper()

    # generate wordlist and result linked list
    wordRank = pd.read_csv("wordRank.csv")
    wordList = list(wordRank["Word"])
    result = LinkedList()
    for i in wordList: # Generate result list based on good bad and known letters
        word = list(i)
        flag = 1
        if len(good) > 0:
            for j in good:
                if j not in word:
                    flag = 0
        if len(bad) > 0:
            for j in bad:
                if j in word:
                    flag = 0
        if len(first) > 0:
            if word[0] != first:
                flag = 0
        if len(second) > 0:
            if word[1] != second:
                flag = 0
        if len(third) > 0:
            if word[2] != third:
                flag = 0
        if len(fourth) > 0:
            if word[3] != fourth:
                flag = 0
        if len(fifth) > 0:
            if word[4] != fifth:
                flag = 0
        if flag == 1:
            result.insert("".join(word))

    print("Top possible solutions to this wordle, are given below in order of likelihood.")
    result.print50() # Print first 50 letters


def printTop(prev="",good=[],bad=[],first="",second="",third="",fourth="",fifth=""): # Used by solver to play the game returns only first topmost word
    good = list(set(list(good)))

    bad = list(set(list(bad)))

    first = first.upper()
    second = second.upper()
    third = third.upper()
    fourth = fourth.upper()
    fifth = fifth.upper()


    wordRank = pd.read_csv("wordRank.csv")
    wordList = list(wordRank["Word"])
    for i in wordList:
        word = list(i)
        flag = 1
        if len(good) > 0:
            for j in good:
                if j not in word:
                    flag = 0
        if len(bad) > 0:
            for j in bad:
                if j in word:
                    flag = 0
        if len(first) > 0:
            if word[0] != first:
                flag = 0
        if len(second) > 0:
            if word[1] != second:
                flag = 0
        if len(third) > 0:
            if word[2] != third:
                flag = 0
        if len(fourth) > 0:
            if word[3] != fourth:
                flag = 0
        if len(fifth) > 0:
            if word[4] != fifth:
                flag = 0
        if flag == 1 and "".join(word) not in prev:
            return("".join(word))