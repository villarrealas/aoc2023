import sys
from classes.solver import SolverBase

    # list of str digits which are allowed
str_digits = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

# map of the string values
str_to_int_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

class Calibration(SolverBase):
    '''
    Class for handling Day 1's Trebuchet problem.
    Takes file_path as variable.
    '''

    def solve(self, allow_strings=False):
        '''
        Returns calibration value.
        allow_strings flag shifts between p1 and p2
        '''
        self.store_input()
        res = []
        for line in self.stored_lines:
            print(line)
            # find where existing digits are
            digit_idx = [ind for ind, i in enumerate(line) if i.isdigit()]
            if digit_idx:
                first_idx = digit_idx[0]
                first_digit = line[first_idx]
                last_idx = digit_idx[-1]
                last_digit = line[last_idx]
            else:
                first_idx = len(line) - 1
                last_idx = 0
            if allow_strings == True:
                for str_digit in str_digits:
                    fval = line.find(str_digit)
                    if fval != -1 and fval <= first_idx:
                        first_idx = fval
                        first_digit = str_to_int_map[str_digit]
                    lval = line.rfind(str_digit)
                    if lval != -1 and lval >= last_idx:
                        last_idx = lval
                        last_digit = str_to_int_map[str_digit]
            res.append(int(first_digit+last_digit))
        return sum(res)

    def value(self, allow_strings=False):
        return self.solve(allow_strings)
        

if __name__ == "__main__":
    file_path = sys.argv[1]
    string_var_choice = sys.argv[2]

    calibration = Calibration(file_path)
    print(calibration.value(allow_strings=string_var_choice))