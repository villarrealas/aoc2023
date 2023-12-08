from aoc2023.classes.solver import SolverBase
import re
from itertools import cycle
from multiprocessing import Pool

class Junction():
    '''
    Helper class for a junction.
    '''
    def __init__(self, junction_name, junction_left, junction_right):
        self.junction_name = junction_name
        self.junction_left = junction_left
        self.junction_right = junction_right
        # junction value: -1 for start, 1 for end, 0 otherwise
        if junction_name[-1] == 'A':
            self.value = -1
        elif junction_name[-1] == 'Z':
            self.value = 1
        else:
            self.value = 0

    def turn(self, turndir):
        if turndir == 'L':
            return self.junction_left
        else:
            return self.junction_right
        
    def __add__(self, other):
        return self.value + other
    
    def __radd__(self,other):
        return self.value + other

class Day8Solver(SolverBase):
    '''
    Check which game states are possible or not.
    '''
    def method_p1(self):
        self.store_input()

        lines = self.stored_lines
        directions = cycle([char for char in lines[0].strip()])
        junction_l = dict()
        junction_r = dict()
        for line in lines[2:]:
            junction, nextparts = line.split('=')
            junction = junction.strip()
            parts_l, parts_r = nextparts.split(',')
            parts_l = parts_l.strip().strip('(')
            parts_r = parts_r.strip().strip(')')
            junction_l[junction] = parts_l
            junction_r[junction] = parts_r
        
        current_junction = 'AAA'
        target_junction = 'ZZZ'
        steps = 0
        for nextdir in directions:
            if nextdir == 'L':
                current_junction = junction_l[current_junction]
            else:
                current_junction = junction_r[current_junction]
            steps = steps + 1
            if current_junction == target_junction:
                break
        
        return steps

    def method_p2(self):
        self.store_input()

        lines = self.stored_lines
        directions = cycle([char for char in lines[0].strip()])
        junction_l = dict()
        junction_r = dict()
        for line in lines[2:]:
            junction, nextparts = line.split('=')
            junction = junction.strip()
            parts_l, parts_r = nextparts.split(',')
            parts_l = parts_l.strip().strip('(')
            parts_r = parts_r.strip().strip(')')
            junction_l[junction] = parts_l
            junction_r[junction] = parts_r
        
        junction_keys = list(junction_l.keys())
        current_junctions = [junction_key for junction_key in junction_keys if junction_key[-1] == 'A']
        target_junction_end = 'Z'
        steps = 0
        for nextdir in directions:
            if nextdir == 'L':
                current_junctions = [junction_l[cjunction] for cjunction in current_junctions]
            else:
                current_junctions = [junction_r[cjunction] for cjunction in current_junctions]
            steps = steps + 1
            test_junctions = [junction for junction in current_junctions if junction[-1] == target_junction_end]
            if test_junctions and len(test_junctions) == len(current_junctions):
                break
        return steps

    def method_p2_alt(self):
        self.store_input()

        lines = self.stored_lines
        directions = cycle([char for char in lines[0].strip()])
        junction_list = dict()
        for line in lines[2:]:
            junction, nextparts = line.split('=')
            junction = junction.strip()
            parts_l, parts_r = nextparts.split(',')
            parts_l = parts_l.strip().strip('(')
            parts_r = parts_r.strip().strip(')')
            junction_list[junction] = Junction(junction, parts_l, parts_r)
        current_junctions = [junction for junction in junction_list.values() if junction.value == -1]
        start_sum = len(current_junctions)
        steps = 0
        for nextdir in directions:
            current_junctions = [junction_list[junction.turn(nextdir)] for junction in current_junctions]
            steps = steps + 1
            test_sum = sum(current_junctions)
            if test_sum == start_sum:
                break

        return steps
    
    def walk_junction_l(self, current_junction):
        new_junction = current_junction.turn('L')
        return new_junction

    def walk_junction_r(self, current_junction):
        new_junction = current_junction.turn('R')
        return new_junction

    def method_p2_mt(self):
        self.store_input()

        lines = self.stored_lines
        directions = cycle([char for char in lines[0].strip()])
        junction_list = dict()
        for line in lines[2:]:
            junction, nextparts = line.split('=')
            junction = junction.strip()
            parts_l, parts_r = nextparts.split(',')
            parts_l = parts_l.strip().strip('(')
            parts_r = parts_r.strip().strip(')')
            junction_list[junction] = Junction(junction, parts_l, parts_r)
        current_junctions = [junction for junction in junction_list.values() if junction.value == -1]
        start_sum = len(current_junctions)
        steps = 0
        pool = Pool()
        for nextdir in directions:
            if nextdir == 'L':
                next_junctions = pool.map(self.walk_junction_l, current_junctions)
            else:
                next_junctions = pool.map(self.walk_junction_r, current_junctions)
            current_junctions = [junction_list[junction] for junction in next_junctions]
            steps = steps + 1
            test_sum = sum(current_junctions)
            if test_sum == start_sum:
                break

        return steps

    def solve_p1(self):
        val = self.method_p1()
        return val

    def solve_p2(self):
        val = self.method_p2()
        return val
    
    def solve_p2_alt(self):
        val = self.method_p2_alt()
        return val

    def solve_p2_mt(self):
        val = self.method_p2_mt()
        return val

if __name__ == "__main__":
    solver = Day8Solver('day8/input.txt')
    res = solver.solve_p2_mt()
    print(res)

            

