class statistics:
    def update_trial(self):
        self.__new_games_played_count

    def update_trial_upon_win(trial_number):
        lines = []
        with open('statistics.txt', 'r+') as file_pointer:
            content = file_pointer.readlines()
            trial_stat = content[trial_number]
            content[trial_number] = str(int(trial_stat) + 1) + '\n'
            lines = content
            file_pointer.close()

        with open('statistics.txt', 'w') as file_pointer:
            file_pointer.writelines(lines)
            file_pointer.close()


    def increment_total_games_played(self):
        with open('statistics.txt', 'r+') as file_pointer:
            content = file_pointer.read().split('\n')
            games_played = content[0]
            new_games_played_count = int(games_played) + 1
            file_pointer.seek(0)
            file_pointer.write(str(new_games_played_count) + '\n')
            file_pointer.close()
            return self.new_games_played_count()


    def get_win_percentage(self):
        with open('statistics.txt', 'r+') as file_pointer:
            content = file_pointer.readlines()
            total_games_played = int(content[0])
            trial_data = content[1:]
            total_wins = 0
            for trial in trial_data:
                total_wins += int(trial)
            return self.float(total_wins / total_games_played)


    def get_guess_distribution(self):
        with open('statistics.txt', 'r+') as file_pointer:
            content = file_pointer.readlines()
            trial_data = content[1:]
            return [int(i) for i in trial_data]