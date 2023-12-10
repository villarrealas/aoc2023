from aoc2023.classes.solver import SolverBase
from itertools import combinations

def twopathcombine(possible_paths):
    starting_paths = list(combinations(possible_paths,2))
    return starting_paths

def map_point(x, y):
    return str(x) + ',' + str(y)

def new_map_point(x,y,direction):
    if direction == 'N':
        return x, y-1
    if direction == 'S':
        return x, y+1
    if direction == 'W':
        return x-1, y
    if direction == 'E':
        return x+1, y
    
def opp_path(direction):
    if direction == 'N':
        return 'S'
    elif direction == 'S':
        return 'N'
    elif direction == 'W':
        return 'E'
    elif direction == 'E':
        return 'W'
    else:
        print('error!')
        return None

class Map():
    def __init__(self, lines):
        self.lines = lines
        self.map = dict()
        self.xmin = 0
        self.xmax = len(lines[0])-1
        self.ymin = 0
        self.ymax = len(lines)-1
        for y in range(self.ymax+1):
            for x in range(self.xmax+1):
                self.map[map_point(x,y)] = lines[y][x]
                if lines[y][x] == 'S':
                    self.animal_start = [x,y]
    
    # all possible chars:  |, -, L, J, 7, F
    def valid_paths(self, x, y):
        valid_paths = []
        mychar = self.map[map_point(x,y)]
        if mychar == '|':
            mychecks = ['N', 'S']
        elif mychar == '-':
            mychecks = ['W', 'E']
        elif mychar == 'L':
            mychecks = ['N','E']
        elif mychar == 'J':
            mychecks = ['W', 'N']
        elif mychar == '7':
            mychecks = ['W', 'S']
        elif mychar == 'F':
            mychecks = ['E', 'S']
        elif mychar == 'S':
            mychecks = ['N', 'S', 'W', 'E']
        else:
            mychecks = []

        # check north
        if y > 0 and 'N' in mychecks:
            if self.map[map_point(x,y-1)] in ['F','7','|','S']:
                valid_paths.append('N')

        # check south
        if y < self.ymax and 'S' in mychecks:
            if self.map[map_point(x,y+1)] in ['L','J','|','S']:
                valid_paths.append('S')

        # check west
        if x > 0 and 'W' in mychecks:
            if self.map[map_point(x-1,y)] in ['F','-','L','S']:
                valid_paths.append('W')

        # check east
        if x < self.xmax and 'E' in mychecks:
            if self.map[map_point(x+1,y)] in ['7','-','J','S']:
                valid_paths.append('E')

        return valid_paths


class Day10Solver(SolverBase):
    '''
    Check which game states are possible or not.
    '''
    def method_p1(self):
        self.store_input()
        lines = self.stored_lines
        pipe_map = Map(lines)
        starting_x, starting_y = pipe_map.animal_start
        starting_path_options = pipe_map.valid_paths(starting_x, starting_y)
        all_starting_options = twopathcombine(starting_path_options)
        print(all_starting_options, starting_x, starting_y)
        for starting_options in all_starting_options:
            new_x1, new_y1 = new_map_point(starting_x, starting_y, starting_options[0])
            backpath1 = opp_path(starting_options[0])
            new_x2, new_y2 = new_map_point(starting_x, starting_y, starting_options[1])
            backpath2 = opp_path(starting_options[1])

            old_x1, old_y1 = -1, -1
            old_x2, old_y2 = -1, -1
            steps = 1
            walkover = False
            valid_loop = True
            while walkover == False:
                newpath1 = [path for path in pipe_map.valid_paths(new_x1, new_y1) if path not in backpath1]
                print(new_x1, new_y1, backpath1, newpath1)
                newpath2 = [path for path in pipe_map.valid_paths(new_x2, new_y2) if path not in backpath2]
                steps = steps+1
                if not newpath1 or not newpath2:
                    print('no possible paths')
                    break
                backpath1 = opp_path(newpath1[0])
                backpath2 = opp_path(newpath2[0])
                old_x1, old_y1 = new_x1, new_y1
                old_x2, old_y2 = new_x2, new_y2
                
                new_x1, new_y1 = new_map_point(old_x1, old_y1, newpath1[0])
                new_x2, new_y2 = new_map_point(old_x2, old_y2, newpath2[0])

                if (new_x1, new_y1) == (old_x2, old_y2):
                    walkover = True
                if (new_x1, new_y1) == (new_x2, new_y2):
                    walkover = True

            if walkover == True:
                return(steps)
        print('no path found')
        return None

    def method_p2(self):
        self.store_input()

    def solve_p1(self):
        val = self.method_p1()
        return val

    def solve_p2(self):
        val = self.method_p2()
        return val
    

if __name__ == "__main__":
    solver = Day10Solver('day10/input.txt')
    res = solver.solve_p1()
    print(res)

            

