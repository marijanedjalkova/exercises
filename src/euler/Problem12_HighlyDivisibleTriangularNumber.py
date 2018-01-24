divisors_dict = {}


def get_next_triangle_number(current_triangle_number, number_to_add):
    return current_triangle_number + number_to_add, number_to_add + 1


def num_of_divisors(number):
    if number in divisors_dict:
        return divisors_dict[number]
    if number == 1:
        return 1
    # every number is divisible by 1 and itself
    counter = 2
    current_divisor = 2
    while current_divisor <= number / current_divisor:
        if number % current_divisor == 0:
            counter += 2
        current_divisor += 1
    divisors_dict[number] = counter
    return counter


def get_number_with_over_n_divisors(n):
    triangle_number = 1
    number_to_add = 2
    number_of_divisors = num_of_divisors(n)
    while number_of_divisors <= n:
        print(triangle_number, number_of_divisors)
        triangle_number, number_to_add = get_next_triangle_number(triangle_number, number_to_add)
        number_of_divisors = num_of_divisors(triangle_number)
    return triangle_number


def tests():
    test_list = [(num_of_divisors(1) == 1),
                 (num_of_divisors(3) == 2),
                 (num_of_divisors(6) == 4),
                 (num_of_divisors(10) == 4),
                 (num_of_divisors(15) == 4),
                 (num_of_divisors(21) == 4),
                 (num_of_divisors(28) == 6),
                 (get_number_with_over_n_divisors(5) == 28)]
    res = all(test_list)
    if not res:
        print(test_list)
    return res


if __name__ == "__main__":
    print("Problem 12:")
    print("Tests pass: ", tests())
    print(get_number_with_over_n_divisors(500))

