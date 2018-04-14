def get_num_of_divisors(in_number):
    divisors = set()
    divisors.add(1)
    upper_limit = in_number // 2 + 1
    current_num = 2
    while current_num <= upper_limit:
        if not in_number % current_num:
            divisors.add(current_num)
            divisors.add(in_number // current_num)
            upper_limit = in_number // current_num - 1
        current_num += 1
    return len(divisors)


def apply_custom_formula(a, b, n):
    return n*n + a*n + b


known_primes = set()
known_primes.add(1)
known_primes.add(2)


def is_prime(num):
    if num < 0:
        return False
    if num in known_primes:
        return True
    if get_num_of_divisors(num) == 1:
        known_primes.add(num)
        return True
    return False


def get_custom_prime_sequence_length(a, b, current_max_length):
    # check if n = max_length gives a prime number for this new formula
    if not is_prime(b):
        # no chance, b has to be prime
        return -1
    if not is_prime(apply_custom_formula(a, b, current_max_length)):
        # no improvement over the previous result
        return -1
    # check all the previous numbers
    for n in range(current_max_length):
        if not is_prime(apply_custom_formula(a, b, n)):
            return n
    # Check the next ones
    n = current_max_length + 1
    while is_prime(apply_custom_formula(a, b, n)):
        print(a, b, n)
        n += 1
    return n


def get_best_formula():
    max_length = 40
    max_a = 0
    max_b = 0
    for a in range(-999, 1000):
        for b in range(2, 1001):
            if not a % 100 and not b % 100:
                print(a, b, max_length)
            length = get_custom_prime_sequence_length(a, b, max_length)
            if length > max_length:
                max_length = length
                max_a = a
                max_b = b
    print_res(max_length, max_a, max_b)


def print_res(max_length, max_a, max_b):
    a_sign = "+" if max_a >= 0 else ""
    b_sign = "+" if max_b >= 0 else ""
    print(max_length, "<= n^2{}{}n{}{}".format(a_sign, max_a, b_sign, max_b))
    print("Result is ", max_a * max_b)


def tests():
    res = get_custom_prime_sequence_length(-79, 1601, 79)
    print(res)


if __name__ == "__main__":
    # tests()
    get_best_formula()
