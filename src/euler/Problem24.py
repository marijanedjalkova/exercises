from math import factorial

digits = list(range(10))


def get_nth_in_permutation(given):
    res = []
    remaining = given - 1
    current_delta = 0
    for i in range(10):
        remaining -= current_delta
        change_number = factorial(10 - i - 1)
        num_of_shifts = remaining // change_number
        current_delta = change_number * num_of_shifts
        res.append(digits[num_of_shifts])
        digits.remove(digits[num_of_shifts])
    return res


print(get_nth_in_permutation(1000000))
