def tests():
    test1 = (get_divisor_sum(220) == 284)
    test2 = (get_divisor_sum(284) == 220)
    test3 = (are_amicable(220, 284))
    test_list = [test1, test2, test3]
    return all(test_list)


def get_divisor_sum(in_number):
    divisors = [1]
    upper_limit = in_number // 2 + 1
    current_num = 2
    while current_num <= upper_limit:
        if not in_number % current_num:
            divisors.append(current_num)
            divisors.append(in_number // current_num)
            upper_limit = in_number // current_num - 1
        current_num += 1
    return sum(divisors)


def are_amicable(num1, num2, sum1=None):
    if num1 == num2:
        return False
    if not sum1:
        sum1 = get_divisor_sum(num1)
    sum2 = get_divisor_sum(num2)
    return sum1 == num2 and sum2 == num1


def get_sum_amicable_under(in_number):
    res = 0
    done_lst = []
    for num in range(in_number):
        if num not in done_lst:
            divisor_sum = get_divisor_sum(num)
            if are_amicable(num, divisor_sum, divisor_sum):
                print("Amicable: {0} and {1}".format(num, divisor_sum))
                res += num
                done_lst.append(num)
                res += divisor_sum
                done_lst.append(divisor_sum)
    return res


if __name__ == "__main__":
    print(tests())
    print(get_sum_amicable_under(10000))
