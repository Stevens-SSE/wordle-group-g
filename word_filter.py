class World_filter:
    def valid_words(self):
        self.__wordslist
    def get_valid_words():
        with open('words.txt', 'r+') as file_pointer:
            content = file_pointer.read().split('\n')
            file_pointer.close()
            words_list = []
            for word in content:
                if len(word) != 5:
                    continue
                words_list.append(word)
            return self.valid_words()


    def write_words_list_to_file(words_list):
        with open('valid_words.txt', 'w') as file_pointer:
            file_pointer.writelines([str(i) + '\n' for i in words_list])
            file_pointer.close()


    def main():
        words_list = get_valid_words()
        write_words_list_to_file(words_list)


    if __name__ == "__main__":
        main()
