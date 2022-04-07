import logging
import csv
from collections import OrderedDict


def log_to_file(level, message):
    logging.basicConfig(filename='app.log', filemode='a+', format='%(levelname)s - %(message)s', level=logging.DEBUG)
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    else:
        logging.warning(message)


def order(trials, user_input):  # function for making file for storing in csv
    letter_dictionary = OrderedDict()
    alphabets = [str(i) for i in 'abcdefghijklmnopqrstuvwxyz']  # compare to every letter
    for letter in alphabets:
        letter_dictionary[letter] = [0, 0, 0, 0, 0]  # each index frequency
    while trials > 0:
        for index in range(len(user_input)):
            temp = letter_dictionary[user_input[index]]
            index = index + 1
        trials -= 1
    for letter in letter_dictionary:
        separated_letters = ('%s -> %s' % (letter, letter_dictionary[letter]))  # seperate letter and occurence

    with open('letterFrequency.csv', 'w') as csvfile:                           #storing in csv file
        writer = csv.DictWriter(csvfile, fieldnames=letter_dictionary.keys())      # writing into csv file the letter
        # and occurance
        writer.writeheader()
        writer.writerows(letter_dictionary)             #row output


# Converting into list of tuple
    list = list(letter_dictionary.items())

if __name__ == "__main__":
    order()
