def find_power_digit_sum(base, power):
    number = pow(base, power)
    return get_digit_sum(number)


def get_digit_sum(number):
    if number < 10:
        return number
    return number % 10 + get_digit_sum(number // 10)


def tests():
    test_list = [find_power_digit_sum(2, 15) == 26,
                 find_power_digit_sum(2, 3) == 8,
                 find_power_digit_sum(2, 0) == 1,
                 find_power_digit_sum(2, 4) == 7]
    res = all(test_list)
    if not res:
        print(test_list)
    return res


if __name__ == "__main__":
    print(tests())
    print(find_power_digit_sum(2, 1000))
