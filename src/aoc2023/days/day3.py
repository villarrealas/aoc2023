from aoc2023.classes.solver import SolverBase
import re

class Day3Solver(SolverBase):
    '''
    Solver for Day3.
    '''
    def store_schematic(self):
        '''Read lines from an input file to stored_schem property.'''
        f = open(self.path_to_file)
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in lines]
        # find length of map in x
        self.num_cols = len(lines[0])
        self.num_rows = len(lines)
        schematic = [[0]*self.num_cols for _ in range(self.num_rows)]
        y_idx = 0
        for line in lines:
            x_idx = 0
            for i in line:
                schematic[y_idx][x_idx] = i
                x_idx = x_idx + 1
            y_idx = y_idx + 1
        self.stored_schem = schematic
        
        # now that we have a whole schematic, look for adjacencies
        symbtest = re.compile('[.^0-9a-zA-Z]+')
        parts = [[False]*self.num_cols for _ in range(self.num_rows)]
        y_idx = 0
        for line in lines:
            x_idx = 0
            for i in line:
                value = schematic[y_idx][x_idx]
                if value.isdigit():
                    found_symbol = False
                    for y_test in range(y_idx - 1, y_idx + 2):
                        for x_test in range(x_idx - 1, x_idx + 2):
                            if y_test >= 0 and y_test < self.num_rows:
                                if x_test >= 0 and x_test < self.num_cols:
                                    if x_test != 0 and y_test != 0:
                                        test_val = schematic[y_test][x_test]
                                        symbfind = re.compile('[^0-9a-zA-Z.]+')
                                        if symbfind.search(test_val):
                                            found_symbol = True
                    if found_symbol == True:
                        parts[y_idx][x_idx] = True
                x_idx = x_idx + 1
            y_idx = y_idx + 1
        self.stored_parts = parts

    def method(self):
        self.store_schematic()
        valid_nums = []
        for row in range(self.num_rows):
            schem_line = self.stored_schem[row]
            part_line = self.stored_parts[row]
            started_num = False
            valid_part = False
            for i, part in zip(schem_line, part_line):
                if i.isdigit():
                    if started_num == False:
                        num_str = ''
                        started_num = True
                    num_str = num_str + i
                    if part == True:
                        valid_part = True
                else:
                    if valid_part == True:
                        valid_nums.append(int(num_str))
                        valid_part = False
                    started_num = False
            if valid_part == True:
                valid_nums.append(int(num_str))
                valid_part = False
        return sum(valid_nums)

    def gear_method(self):
        self.store_schematic()
        gear_ratios = []
        # dumb idea to associate numbers w/ 2d array
        schem_nums = []
        part_idxs = [[-1]*self.num_cols for _ in range(self.num_rows)]
        part_idx = 0
        num_flag = False
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                val = self.stored_schem[row][col]
                if val.isdigit():
                    if num_flag == False:
                        num_flag = True
                        num_str = ''
                    num_str = num_str + val
                else:
                    if num_flag == True:
                        backwrite = len(num_str)
                        for col_write in range(col-backwrite, col):
                            part_idxs[row][col_write] = part_idx
                        schem_nums.append(int(num_str))
                        part_idx = part_idx + 1
                        num_flag = False
            if num_flag == True:
                backwrite = len(num_str)
                for col_write in range(col-backwrite, col):
                    part_idxs[row][col_write] = part_idx
                schem_nums.append(int(num_str))
                part_idx = part_idx + 1
                num_flag = False
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                symbfind = re.compile('[*]')
                if symbfind.search(self.stored_schem[row][col]):
                    part_nums = []
                    for y_test in range(row-1, row+2):
                        for x_test in range(col-1, col+2):
                            part_num = part_idxs[y_test][x_test]
                            if part_num != -1:
                                part_nums.append(part_num)
                    part_nums = list(set(part_nums))
                    if len(part_nums) == 2:
                        gear_ratio = schem_nums[part_nums[0]]*schem_nums[part_nums[1]]
                        gear_ratios.append(gear_ratio)
        return sum(gear_ratios)

    def solve(self):
        return self.method()
    
    def solve_gr(self):
        return self.gear_method()

if __name__ == "__main__":
    solver = Day3Solver('day3/input1.txt')
    res = solver.solve_gr()
    print(res)

            

