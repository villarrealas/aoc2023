from aoc2023.classes.solver import SolverBase
import re
from multiprocessing import Pool

class Day5Solver(SolverBase):
    '''
    Solver for Day5.
    '''
    def store_almanac(self):
        f = open(self.path_to_file)
        readlines = [line.rstrip('\n') for line in f.readlines()]

        # first we reed the seeds
        self.seeds = re.findall('\d+', readlines[0])

        map_lines = readlines[2:]

        map_names = []
        map_lists = []

        # then we store maps
        start_map = False
        for line in map_lines:
            if start_map == False:
                start_map = True
                map_name = line.split(' ')[0]
                map_names.append(map_name)
                map_list = []
            else:
                if line:
                    dest_start, source_start, range_len = line.split(' ')
                    map_list.append([source_start, dest_start, range_len])
                else:
                    start_map = False
                    map_lists.append(map_list)
        map_lists.append(map_list)
        self.stored_map_names = map_names
        self.stored_map_lists = map_lists

    def sort_last_map_list(self):
        map_lists = self.stored_map_lists
        last_maps = map_lists.pop()
        last_maps = sorted(last_maps, key=lambda x: x[1])
        map_lists.append(last_maps)
        self.sorted_map_lists = map_lists

    def method(self, seed):
        # now we need to find the lowest location value
        # for our given seeds

        val = seed
        for map_lists in self.stored_map_lists:
            found_map = False
            for map_list in map_lists:
                if found_map == False:
                    map_low = int(map_list[0])
                    map_high = int(map_list[0])+int(map_list[2])
                    if map_low <= int(val) < map_high:
                        val = str(int(map_list[1])+(int(val) - map_low))
                        found_map = True

        return int(val)

    def rev_method(self, location):
        # find the smallest valid location

        val = location
        inv_map_lists = self.sorted_map_lists[::-1]
        for map_lists in self.sorted_map_lists[::-1]:
            found_map = False
            for map_list in map_lists:
                if found_map == False:
                    map_low = int(map_list[1])
                    map_high = int(map_list[1])+int(map_list[2])
                    if map_low <= int(val) < map_high:
                        val = str(int(map_list[0])+(int(val)-map_low))
                        found_map = True

        seed_vals = self.seeds
        pair_count = int(len(seed_vals) / 2)
        for i in range(pair_count):
            low_val = int(seed_vals[2*i])
            high_val = low_val + int(seed_vals[2*i+1])
            if low_val <= int(val) < high_val:
                self.location_found = True
                return int(location)
        return 9999999999
            
        
    def find_seeds(self, pair):
        start, amt = pair
        seeds = []
        seeds.extend(range(int(start), int(start)+int(amt)))
        return seeds

    def solve(self):
        self.store_almanac()
        seeds = self.seeds
        pool = Pool()
        vals = pool.map(self.method, seeds)
        return min(vals)

    def solve_oops(self):
        self.store_almanac()
        seed_vals = self.seeds
        pair_count = int(len(seed_vals) / 2)
        pairs = []
        for i in range(pair_count):
            pairs.append([seed_vals[2*i], seed_vals[2*i+1]])
        pool = Pool(4)
        seeds = pool.map(self.find_seeds, pairs)
        seeds = sum(seeds, [])
        vals = pool.map(self.method, seeds)
        return min(vals)
    
    def solve_reverse(self):
        pool = Pool(8)
        self.store_almanac()
        self.sort_last_map_list()
        self.location_found = False
        map_lists = self.stored_map_lists
        location_sets = map_lists[-1]
        min_location_set = int(location_sets[0][1])
        fake_location_set = [ ['0', '0', str(min_location_set)]]
        location_sets = fake_location_set + location_sets
        all_vals = []
        for location_set in location_sets:
            if self.location_found == False:
                locations = []
                src, dest, rng = location_set
                locations.extend(range(int(dest),int(dest)+int(rng)))
                vals = pool.map(self.rev_method, locations)
                all_vals.extend(vals)
        return min(all_vals)

if __name__ == "__main__":
    solver = Day5Solver('day5/input.txt')
    res = solver.solve_reverse()
    print(res)

            

