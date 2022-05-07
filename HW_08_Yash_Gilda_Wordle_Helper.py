
from copy import copy


class Helper:
    '''
    def rankedWords(correctWords, incorrectWords):
        rankDic = {}
        import csv
        with open('/Users/yashgilda/desktopp/MSCS/Sem_2/SSW_810/HW_04/Wordle/wordRank.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                rankDic[row[0].split(',')[0]] = row[1].split(',')[0]
        rankDic.pop('Rank')
        myList = []
        defaultList = []
        if correctWords == None and incorrectWords == None:
            for i in range(1,51):
                defaultList.append(rankDic[str(i)])
            return defaultList
        if correctWords != None:
            for key in range(1,len(rankDic)):
                flag = 0
                for letter in correctWords:
                    if letter not in rankDic[str(key)]:
                        flag = 1
                if flag == 0:
                    myList.append(rankDic[str(key)])
        else:
            for key in rankDic:
                myList.append(rankDic[key])
        defaultList = myList.copy()
        if incorrectWords != None:
            for word in myList:
                flag = 0
                for letter in incorrectWords:
                    if letter in word:
                        flag = 1
                if flag == 1:
                    defaultList.remove(word)
        return defaultList

        '''

    #testcall to check the function is working right
    #print(rankedWords(['t','r','s'],['b','o','l','i','e']))

    def printTop(prev="",goodLetters=[],badLetters=[],first="",second="",third="",fourth="",fifth=""): # Used by solver to play the game returns only first topmost word
        goodLetters = list(set(list(goodLetters)))

        badLetters = list(set(list(badLetters)))

        #first = first.upper()
        #second = second.upper()
        #third = third.upper()
        #ourth = fourth.upper()
        #fifth = fifth.upper()

        rankDic = {}
        import csv
        with open('/Users/yashgilda/desktopp/MSCS/Sem_2/SSW_810/HW_04/Wordle/wordRank.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                rankDic[row[0].split(',')[0]] = row[1].split(',')[0]
        rankDic.pop('Rank')
        #wordRank = pd.read_csv("wordRank.csv")
        #wordList = list(rankDic["Word"])
        wordList = list(rankDic.values())
        for i in wordList:
            word = list(i)
            flag = 1
            if len(goodLetters) > 0:
                for j in goodLetters:
                    if j not in word:
                        flag = 0
            if len(badLetters) > 0:
                for j in badLetters:
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
