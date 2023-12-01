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

str_digits_backwards = [
    'eno',
    'owt',
    'eerht',
    'ruof',
    'evif',
    'xis',
    'neves',
    'thgie',
    'enin',
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

# open our file
file = "input.txt"
f = open(file, "r")

# string comprehension for digits in line
all_digits = []
for line in f:
    # find where all the digits are
    digit_idx = [ind for ind, i in enumerate(line) if i.isdigit()]
    # check if there is a string digit closer than the first digit
    if digit_idx:
        first_idx = digit_idx[0]
        first_digit = line[first_idx]
        last_idx = digit_idx[-1]
        last_digit = line[last_idx]
    else:
        first_idx = len(line) -1
        first_digit = 0
        last_idx = 0
        last_digit = 0
    for str_digit in str_digits:
        val = line.find(str_digit, 0, first_idx+2)
        if val != -1 and val <= first_idx:
            first_idx = val
            first_digit = str_to_int_map[str_digit]
    # then we're going to do the dumbest thing ever and
    # invert the string
    inv_line = line[::-1]
    # and now repeat the above nonsense
    last_idx_inv  = len(line) - last_idx
    for str_digit_bw in str_digits_backwards:
        val = inv_line.find(str_digit_bw, 0, len(line) - last_idx + 2)
        if val != -1 and val <= last_idx_inv:
            last_idx_inv = val
            last_digit = str_to_int_map[str_digit_bw[::-1]]
    # append the digits
    all_digits.append(int(first_digit+last_digit))

print(all_digits)

# sum the digits
sum_digits = sum(all_digits)

# print it up
print(sum_digits)
    
