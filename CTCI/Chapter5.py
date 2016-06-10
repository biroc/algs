"""
5.1 Insertion
"""
def insertion(N,M,i,j):
    one_mask = ~0
    left_mask = one_mask << (j+1)
    right_mask = (1 << i) - 1
    mask = left_mask | right_mask
    n_cleared = N & mask
    m_shifted = M << i
    return n_cleared | m_shifted

"""
5.2 Binary to String
Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with at most 32 characters, print "ERROR"
"""
def convert_binary(number):
    string = "."
    while number > 0:
        r = number * 2 # shift the number to the left one bit
        if r >= 1: # if the number is greater than 1, that left-most bit was 1
            string += "1"
            number = r - 1 # set the value to the remaining value
        else:
            string += "0" # if the number is 0 or below 0, the left-most bit was 0
            number = r # set the number to the remaining value

    if len(string) <= 32:
        return string
    else:
        print('ERROR')

"""
5.3
You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1s you could create.
"""
def largest_flip(number):
    largest = head = tail = 0
    while number:
        r = number % 2
        if r == 0:
            largest = max(largest, head+tail+1)
            head = tail
            tail = 0
        else:
            tail += 1
        number >> 1
    if tail:
        largest = max(largest, head+tail+1)
    return largest

"""
5.4 Next Number
Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
"""

# 1
def get_bit(num,i):
    return (num & (1 << i)) != 0


def ones_count(number):
    ones = 0
    for i in range(32):
        if get_bit(number, i):
            ones += 1

    return ones


def find_next(number):
    found = False
    ones = ones_count(number)
    num = number + 1
    while not found:
        ones_found = ones_count(num)
        if ones_found == ones:
            found = True
            return num
        num += 1
    return num

# 2
def find_next2(number):
    zeros = ones = 0
    temp = number
    while temp and (temp & 1) == 0:
        zeros += 1
        temp >>= 1
    while temp & 1 == 1:
        ones += 1
        temp >>= 1

    switch_position = zeros + ones

    number |= 1 << switch_position
    number &= ~ ((1 << switch_position) - 1) # clear
    number |= (1 << (ones - 1)) - 1 #add 1s
    return number


def find_prev2(number):
    zeros = ones = 0
    temp = number
    while (temp & 1) == 1:
        ones += 1
        temp >>= 1

    while temp and (temp & 1) == 0:
        zeros += 1
        temp >>= 1

    switch_pos = zeros + ones
    number &= ((~0) << (switch_pos+1)) # clear pos + 1 positions
    number |= ((1 << (ones + 1)) - 1) << (zeros -1)
    return number

"""
5.5 Debugger: = is power of 2.
"""
def is_pow2(num):
    if num > 0 and (num & (num-1)) == 0:
        return True
    return False
"""
5.6 Conversion
Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.
"""
def num_flips(num1,num2):
    flips = 0
    for i in range(32):
        if get_bit(num1,i) != get_bit(num2,i):
            flips += 1
    return flips


def num_flips2(a,b):
    xored = a ^ b
    count = 0
    while xored:
        if xored & 1 == 1:
            count += 1
        xored >>= 1
    return count


def num_flips3(a,b):
    xored = a ^ b
    count = 0
    while xored:
        count += 1
        xored &= (xored-1)
    return count

"""
5.7 Pairwise Swap
"""
def swap_pairs(num):
    even_bits = (num & 0xAA) >> 1
    odd_bits = (num & 0x55) << 1
    return even_bits | odd_bits


