from aoc2023.classes.solver import SolverBase
import re

class GameChecker(SolverBase):
    '''
    Check which game states are possible or not.
    '''

    def compare_maxes(self, true_max_r, true_max_g, true_max_b):
        self.store_input()
        idx = 1
        good_game_sum = 0
        for line in self.stored_lines:
            game_possible = True
            max_b = 0
            max_r = 0
            max_g = 0
            # parse out what the max was for each game
            splits = line.split(': ')[1].split('; ')
            for game in splits:
                pulls = game.split(', ')
                for pull in pulls:
                    pull_value = int(re.findall('\d+', pull)[0])
                    if pull.find('blue') != -1:
                        if pull_value > max_b:
                            max_b = pull_value
                    elif pull.find('red') != -1:
                        if pull_value > max_r:
                            max_r = pull_value
                    elif pull.find('green') != -1:
                        if pull_value > max_g:
                            max_g = pull_value
                    else:
                        print('something went wrong')
                if max_b > true_max_b or max_g > true_max_g or max_r > true_max_r:
                    game_possible = False
            if game_possible == True:
                good_game_sum = good_game_sum + idx
            idx = idx + 1
        return good_game_sum
 
    def find_power(self):
        self.store_input()
        idx = 1
        power_sum = 0
        for line in self.stored_lines:
            max_b = 0
            max_r = 0
            max_g = 0
            # parse out what the max was for each game
            splits = line.split(': ')[1].split('; ')
            for game in splits:
                pulls = game.split(', ')
                for pull in pulls:
                    pull_value = int(re.findall('\d+', pull)[0])
                    if pull.find('blue') != -1:
                        if pull_value > max_b:
                            max_b = pull_value
                    elif pull.find('red') != -1:
                        if pull_value > max_r:
                            max_r = pull_value
                    elif pull.find('green') != -1:
                        if pull_value > max_g:
                            max_g = pull_value
                    else:
                        print('something went wrong')
            power = max_b * max_g * max_r
            power_sum = power_sum + power
        return power_sum

    def solve(self, true_max_r, true_max_g, true_max_b):
        return self.compare_maxes(true_max_r, true_max_g, true_max_b)

if __name__ == "__main__":
    gamechecker = GameChecker('day2/input1.txt')
    res = gamechecker.find_power()
    print(res)

            

