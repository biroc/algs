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
"""
def convert_binary(number):
    string = "0."
    while number > 0:
        r = number * 2
        if r >= 1:
            string += "1"
            number = r - 1
        else:
            string += "0"
            number = r

    if len(string) <= 32:
        return string
    else:
        print('ERROR')

"""
5.3
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


