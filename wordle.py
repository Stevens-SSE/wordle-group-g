from user_interface import *
from dictionary import Dictionary
from statistics import *
from logs import *


class Wordle:  # class for wordle
    def __init__(self, codeword, num_of_trials):
        self.CODEWORD = codeword
        self.trials = num_of_trials

    def start_game(self, user_interface_instance):
        trial = 1
        codeword = self.CODEWORD
        while trial < self.trials:
            user_word = get_input_from_user(trial)
            log_to_file('info', 'Trial %s -> User input: "%s"' % (trial, user_word))

            if not check_if_entered_word_is_valid(user_word):
                print('Please enter a 5-letter word!')
                log_to_file('error', 'User entered invalid word')
                continue

            if has_user_guessed_the_right_word(user_word, codeword):
                print('You guessed the right word!!!')
                update_trial_upon_win(trial)
                log_to_file('info', 'User guessed the right word!!!')
                break

            if not Dictionary.check_if_word_exists('valid_words.txt', user_word):
                print('Warning! Please provide a valid dictionary word!')
                log_to_file('error', 'User entered invalid word')
                continue

            print('The word you entered -> %s' % user_word)
            user_word = user_word.lower()

            position_arr = position_check_for_letters(user_word, codeword)
            validate_letter_position(position_arr, user_word)
            trial += 1
        self.post_gameplay()  # using class

    def post_gameplay(self):
        codeword = self.CODEWORD
        print('Game over!!! Correct word was %s' % codeword)
        total_games_played = increment_total_games_played()
        print("Total games played are - %s" % total_games_played)
        print('Win percentage: %s' % get_win_percentage())
        log_to_file('info', 'Win percentage: %s' % get_win_percentage())
        guess_distribution = get_guess_distribution()
        for i in range(len(guess_distribution)):
            print('%s -> %s' % (i + 1, guess_distribution[i]))
            log_to_file('info', 'Guess Distribution: Trial #%s -> %s' % (i + 1, guess_distribution[i]))


if __name__ == "__main__":
    dictionary = Dictionary()  # calling  dictioary class
    CODEWORD = dictionary.get_random_word()  # calling random word from dictionary
    Dictionary.add_word_to_used_list(CODEWORD)  # adding used word so that word does not repeat
    log_to_file('info', 'The selected word is "%s"' % CODEWORD)  # logging
    Wordle(codeword=CODEWORD, num_of_trials=7).start_game(user_interface)
