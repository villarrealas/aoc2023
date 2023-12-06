from aoc2023.classes.solver import SolverBase
import re

class Day6Solver(SolverBase):
    '''
    Check which game states are possible or not.
    '''
    def method_p1(self):
        self.store_input()
        lines = self.stored_lines
        times = re.findall('\d+', lines[0])
        distances = re.findall('\d+', lines[1])
        won_races_mult = 1

        for time, distance in zip(times,distances):
            charge_times = range(0,int(time))
            won_races = 0
            for charge_time in charge_times:
                final_dist = charge_time * (int(time) - charge_time)
                if final_dist > int(distance):
                    won_races = won_races + 1
            won_races_mult = won_races_mult * won_races
        
        return won_races_mult

    def method_p2(self):
        self.store_input()
        lines = self.stored_lines
        time = int(''.join(re.findall('\d+', lines[0])))
        distance = int(''.join(re.findall('\d+', lines[1])))

        charge_times = range(0, time)
        won_races = 0
        for charge_time in charge_times:
            final_dist = charge_time * (time - charge_time)
            if final_dist > distance:
                won_races = won_races + 1
        return won_races

    def solve_p1(self):
        val = self.method_p1()
        return val

    def solve_p2(self):
        val = self.method_p2()
        return val


if __name__ == "__main__":
    solver = Day6Solver('day6/input.txt')
    res = solver.solve_p2()
    print(res)

            

