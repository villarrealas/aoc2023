from aoc2023.classes.solver import SolverBase
import re

card_map = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

alt_card_map = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


class Hand():
    def __init__(self, hand, bid):
        self.unsorted_hand = ([card_map[char] for char in hand])
        self.num_hand = sorted([card_map[char] for char in hand], reverse=True)
        self.alt_hand = sorted([alt_card_map[char] for char in hand], reverse=True)
        self.alt_unsorted_hand = ([alt_card_map[char] for char in hand])
        self.bid = int(bid)

    def give_hand_rank(self):
        'cursed hand ranker'
        hand = self.num_hand
        # five of a kind
        if len(set(hand)) == 1:
            self.hand_rank = 6
        elif len(set(hand)) == 2:
            # four of a kind
            if hand.count(hand[0]) == 4:
                self.hand_rank = 5
            elif hand.count(hand[-1]) == 4:
                self.hand_rank = 5
            # only other option is full house
            else:
                self.hand_rank = 4
        # three of a kind
        elif len(set(hand)) == 3:
            if hand.count(hand[0]) == 3:
                self.hand_rank = 3
            elif hand.count(hand[1]) == 3:
                self.hand_rank = 3
            elif hand.count(hand[2]) == 3:
                self.hand_rank = 3
            # otherwise, must be two pair
            else:
                self.hand_rank = 2
        # one pair
        elif len(set(hand)) == 4:
            self.hand_rank = 1
        # notta
        else:
            self.hand_rank = 0
        return self.hand_rank

    def give_hand_rank_joker(self):
        '''tests if hand would be higher with a joker'''
        hand = self.alt_hand
        old_hand_rank = self.give_hand_rank()
        if hand.count(1) == 5:
            new_hand_rank = 6
        elif hand.count(1) == 4:
            new_hand_rank = 6
        elif hand.count(1) == 3:
            if old_hand_rank == 4:
                new_hand_rank = 6
            else:
                new_hand_rank = 5
        elif hand.count(1) == 2:
            if old_hand_rank == 4:
                new_hand_rank = 6
            elif old_hand_rank == 2:
                new_hand_rank = 5
            else:
                new_hand_rank = 3
        elif hand.count(1) == 1:
            if old_hand_rank == 5:
                new_hand_rank = 6
            elif old_hand_rank == 3:
                new_hand_rank = 5
            elif old_hand_rank == 2:
                new_hand_rank = 4
            elif old_hand_rank == 1:
                new_hand_rank = 3
            else:
                new_hand_rank = 1
        else:
            new_hand_rank = 0
        if new_hand_rank >= old_hand_rank:
            return new_hand_rank
        else:
            return old_hand_rank
            
    def give_high_card(self, idx):
        return self.unsorted_hand[idx]
    
    def give_alt_high_card(self, idx):
        return self.alt_unsorted_hand[idx]
    
    def give_sortable(self):
        return ([self.give_hand_rank()] + self.unsorted_hand + [self.bid])

    def give_sortable_joker(self):
        return ([self.give_hand_rank_joker()] + self.alt_unsorted_hand + [self.bid])


class Day7Solver(SolverBase):
    '''
    Check which game states are possible or not.
    '''
    def method_p1(self):
        self.store_input()
        lines = self.stored_lines
        handnbids = []
        for line in lines:
            hand, bid = line.split(' ')
            inst = Hand(hand,bid)
            handnbids.append(inst.give_sortable())

        ordered_handnbids = sorted(handnbids, reverse=True)

        max_rank = len(ordered_handnbids)
        winnings = 0
        for i in range(len(ordered_handnbids)):
            winnings = winnings + (ordered_handnbids[i][-1] * (max_rank - i))
        
        return winnings

    def method_p2(self):
        self.store_input()
        lines = self.stored_lines
        handnbids = []
        for line in lines:
            hand, bid = line.split(' ')
            inst = Hand(hand,bid)
            handnbids.append(inst.give_sortable_joker())

        ordered_handnbids = sorted(handnbids, reverse=True)

        max_rank = len(ordered_handnbids)
        winnings = 0
        for i in range(len(ordered_handnbids)):
            winnings = winnings + (ordered_handnbids[i][-1] * (max_rank - i))
        
        return winnings

    def solve_p1(self):
        val = self.method_p1()
        return val

    def solve_p2(self):
        val = self.method_p2()
        return val


if __name__ == "__main__":
    solver = Day7Solver('day7/input.txt')
    res = solver.solve_p2()
    print(res)

            

