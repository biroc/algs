def answer(numbers):
    if not numbers:
        return 0
    dictionary, index, last_position = {}, 0, 0
    while index not in dictionary:
        dictionary[index] = numbers[index]
        last_position = index
        index = numbers[index]
    pirates = 0
    for x in range(index,last_position+1):
        if x in dictionary:
            pirates += 1
    return pirates