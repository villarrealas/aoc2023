from aoc2023.classes.solver import SolverBase
import re

class Day4Solver(SolverBase):
    '''
    Solver for Day4.
    '''
    def method(self):
        self.store_input()
        sum_vals = 0
        for line in self.stored_lines:
            line = line.split(': ')[1]  
            winning_nums, card_nums = line.split(' | ')
            winning_nums = re.sub('  ', ' ', winning_nums).strip()
            winning_nums = [int(num) for num in winning_nums.split(' ')]
            card_nums = re.sub('  ', ' ', card_nums).strip()
            card_nums = [int(num) for num in card_nums.split(' ')]
            card_val = 0
            for card_num in card_nums:
                if card_num in winning_nums:
                    if card_val == 0:
                        card_val = 1
                    else:
                        card_val = card_val * 2
            sum_vals = sum_vals + card_val
        return sum_vals

    def scratchers(self):
        self.store_input()
        won_cards_all = []
        for line in self.stored_lines:
            line = line.split(': ')[1]  
            winning_nums, card_nums = line.split(' | ')
            winning_nums = re.sub('  ', ' ', winning_nums).strip()
            winning_nums = [int(num) for num in winning_nums.split(' ')]
            card_nums = re.sub('  ', ' ', card_nums).strip()
            card_nums = [int(num) for num in card_nums.split(' ')]
            won_cards = 0
            for card_num in card_nums:
                if card_num in winning_nums:
                    won_cards = won_cards + 1
            won_cards_all.append(won_cards)

        total_cards = [1]*(len(won_cards_all))
        for idx in range(len(won_cards_all)):
            won_cards = won_cards_all[idx]
            won_idx = idx+1
            while won_cards > 0:
                if (won_idx >= len(won_cards_all)):
                    break
                total_cards[won_idx] = total_cards[won_idx] + total_cards[idx]
                won_cards = won_cards - 1
                won_idx = won_idx + 1
        return sum(total_cards)

    def solve(self):
        return self.method()

    def solve_scratchers(self):
        return self.scratchers()
    

if __name__ == "__main__":
    solver = Day4Solver('day4/input.txt')
    res = solver.solve_scratchers()
    print(res)

            

