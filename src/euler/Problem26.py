def tests():
    test_lst = [(get_recurring_cycle_length(2), 0),
                (get_recurring_cycle_length(3), 1),
                (get_recurring_cycle_length(4), 0),
                (get_recurring_cycle_length(6), 1),
                (get_recurring_cycle_length(7), 6),
                (get_recurring_cycle_length(10), 0)]
    res = all([(a == b) for (a, b) in test_lst])
    if not res:
        print(test_lst)
        return
    print("All tests passed")


def get_recurring_cycle_length(num):
    # express the number in lowest terms - done already
    # remove all fractions of 2 and 5
    while not num % 5:
        num //= 5
    while not num % 2:
        num //= 2
    if num == 1:
        return 0
    # find the shortest string of 9s that is divisible by num
    nine_string = 9
    while nine_string % num:
        nine_string = nine_string * 10 + 9
    return len(str(nine_string))


def find_longest_cycle_range(rng):
    max_length = 0
    res = 0
    for n in rng:
        cycle_length = get_recurring_cycle_length(n)
        if cycle_length > max_length:
            max_length = cycle_length
            res = n
    return res, max_length


if __name__ == "__main__":
    tests()
    print(find_longest_cycle_range(range(1, 1000)))
