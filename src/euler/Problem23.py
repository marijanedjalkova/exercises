import time


def get_divisor_sum(in_number):
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
    return sum(divisors)


known_abundant = set()


def is_abundant(in_number):
    if in_number in known_abundant:
        return True
    res = in_number < get_divisor_sum(in_number)
    if res:
        known_abundant.add(in_number)
    return res


def is_not_sum_of2_abundants(number):
    # true if number cannot be written as a sum of two abundant numbers
    # go through known ones and assess the other one
    for item in known_abundant:
        if number - item > 0 and number - item in known_abundant:
            return False
    return True


def find_sum_not_sum_of2_abundants():
    upper_limit = 28123
    total_sum = sum(range(upper_limit+1))
    for i in range(upper_limit+1):
        if not is_not_sum_of2_abundants(i):
            total_sum -= i
    return total_sum


def generate_abundant():
    for i in range(12, 28123):
        if is_abundant(i):
            known_abundant.add(i)
    print("Initialised the dictionary")


if __name__ == "__main__":
    generate_abundant()
    print(find_sum_not_sum_of2_abundants())
