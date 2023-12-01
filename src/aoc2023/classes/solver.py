class SolverBase():
    '''
    A base solver class with some rudimentary
    functionality.
    '''
    def __init__(self, path_to_file):
        '''Initialize SolverBase w/ path to an input file.'''
        # common base path for all stuff here
        path_base = "/Users/sierrav/Repositories/aoc2023/inputs/"
        self.path_to_file = path_base+path_to_file
    
    def store_input(self):
        '''Read lines from an input file to stored_lines property.'''
        f = open(self.path_to_file)
        self.stored_lines = f.readlines()
    
    def solve(self):
        '''Placeholder for solver.'''
        raise NotImplementedError
    
    def value(self):
        '''
        Placeholder for value, calls solver.
        May need additional arguments.
        '''
        return self.solve()

