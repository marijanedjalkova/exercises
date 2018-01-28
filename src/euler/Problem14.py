def get_next_number(n):
    if n % 2 == 0:
        return n / 2
    return 3*n + 1


def get_sequence(starting_number):
    res = [starting_number]
    while starting_number > 1:
        starting_number = get_next_number(starting_number)
        res.append(starting_number)
    return res


def get_starting_number_for_longest_chain():
    starting_number_for_longest_chain = 1
    max_length = 1
    for number in range(1, 1000000):
        if number % 1000 == 0:
            print(number)
        new_length = len(get_sequence(number))
        if new_length > max_length:
            max_length = new_length
            starting_number_for_longest_chain = number
    return starting_number_for_longest_chain, max_length


if __name__=="__main__":
    print("RES ", get_starting_number_for_longest_chain())