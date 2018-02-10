from math import factorial


def find_digit_sum(number):
    res = 0
    num = number
    while num > 0:
        res += num % 10
        num = num // 10
    return res


def find_factorial_digit_sum(number):
    fct = factorial(number)
    return find_digit_sum(fct)


if __name__ == "__main__":
    print(find_factorial_digit_sum(100))