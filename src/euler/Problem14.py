import time

result_dict = {} # starting_number: sequence_length


def get_next_number(n):
    if n % 2 == 0:
        return n / 2
    return 3*n + 1


def get_sequence_length(starting_number):
    first_number = starting_number
    if starting_number in result_dict:
        return result_dict[starting_number]
    sequence = [starting_number]
    already_seen = False
    res = 0
    while starting_number > 1:
        starting_number = get_next_number(starting_number)
        sequence.append(starting_number)
        if starting_number in result_dict:
            # append the number for that to the res
            already_seen = True
            res = len(sequence) - 1 + result_dict[starting_number]
            break
    if not already_seen:
        res = len(sequence)
    result_dict[first_number] = res
    return res


def get_starting_number_for_longest_chain():
    starting_number_for_longest_chain = 1
    max_length = 1
    for number in range(1, 1000000):
        new_length = get_sequence_length(number)
        if new_length > max_length:
            max_length = new_length
            starting_number_for_longest_chain = number
    return starting_number_for_longest_chain, max_length


if __name__=="__main__":
    start_time = time.time()
    print("RES ", get_starting_number_for_longest_chain())
    print("--- %s seconds ---" % (time.time() - start_time))