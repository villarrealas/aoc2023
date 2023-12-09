from aoc2023.classes.solver import SolverBase
import re

def find_diffs(sequence):
    new_sequence = []
    for first, second in zip(sequence[:-1], sequence[1:]):
        new_sequence.append(second - first)
    return new_sequence

class Day9Solver(SolverBase):
    '''
    Check which game states are possible or not.
    '''
    def method_p1(self):
        self.store_input()
        sum_extrapolated = 0
        for history_in in self.stored_lines:
            # store sequences
            history = [int(s) for s in history_in.strip().split(' ')]
            len_history = len(history)
            sequences = [history]
            for i in range(len_history - 1):
                old_sequence = sequences[i]
                new_sequence = find_diffs(old_sequence)
                sequences.append(new_sequence)
                if all(value == 0 for value in new_sequence):
                    break
            # now calculate history
            rev_sequences = sequences[::-1]
            rev_sequences[0].append(0)
            for i in range(len(sequences)-1):
                newvalue = rev_sequences[i][-1] + rev_sequences[i+1][-1]
                rev_sequences[i+1].append(newvalue)
            sum_extrapolated = sum_extrapolated + rev_sequences[-1][-1]
        return sum_extrapolated
                
    def method_p2(self):
        self.store_input()
        sum_extrapolated = 0
        for history_in in self.stored_lines:
            # store sequences
            history = [int(s) for s in history_in.strip().split(' ')]
            len_history = len(history)
            sequences = [history]
            for i in range(len_history - 1):
                old_sequence = sequences[i]
                new_sequence = find_diffs(old_sequence)
                sequences.append(new_sequence)
                if all(value == 0 for value in new_sequence):
                    break
            # now calculate unhistory
            rev_sequences = sequences[::-1]
            rev_sequences[0].append(0)
            for i in range(len(sequences)-1):
                newvalue =  rev_sequences[i+1][0] - rev_sequences[i][0]
                rev_sequences[i+1].insert(0, newvalue)
            sum_extrapolated = sum_extrapolated + rev_sequences[-1][0]
        return sum_extrapolated

    def solve_p1(self):
        val = self.method_p1()
        return val

    def solve_p2(self):
        val = self.method_p2()
        return val
    

if __name__ == "__main__":
    solver = Day9Solver('day9/input.txt')
    res = solver.solve_p2()
    print(res)

            

