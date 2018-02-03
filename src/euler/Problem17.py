def tests():
    test_list = [get_number_of_letters_range(1, 5) == 19,
                 get_number_of_letters_range(342, 342) == 23,
                 get_number_of_letters_range(115, 115) == 20]
    res = all(test_list)
    if not res:
        print(test_list)
    return res


def get_number_of_letters(number):
    if number in word_dict:
        return len(word_dict[number])
    return get_number_of_letters_calculate(number)


def get_number_of_letters_calculate(number):
    # get the last two digits
    thousands = number // 1000 % 10  # e.g. 6 for number 6543
    hundreds = number // 100 % 10  # e.g. 6 for number 7654
    tens = number // 10 % 10  # e.g 6 for number 4762
    ones = number % 10
    res = 0
    res_string = ""
    if thousands:
        phrase = word_dict[thousands] + "thousand"
        res += len(phrase)
        res_string += phrase + " "
    if hundreds:
        phrase = word_dict[hundreds] + "hundred"
        res += len(phrase)
        res_string += phrase + " "
    if (thousands or hundreds) and (tens or ones):
        phrase = "and"
        res += len(phrase)
        res_string += phrase + " "
    if tens == 1:
        phrase = word_dict[tens * 10 + ones]
        res += len(phrase)
        res_string += phrase + " "
    else:
        if tens:
            phrase = word_dict[tens * 10]
            res += len(phrase)
            res_string += phrase + " "
        if ones:
            phrase = word_dict[ones]
            res += len(phrase)
            res_string += phrase + " "
    return res

def process_three(number):
    # this is the {}, a 3-digit number
    # it is definitely less than a thousand
    hundreds = number // 100 % 10  # e.g. 6 for number 7654
    tens = number // 10 % 10  # e.g 6 for number 4762
    ones = number % 10



def smarter(number):
    # every three digits are processed in exactly the same way
    # {} billion {} million {} thousand {}
    pass


def get_number_of_letters_range(start, end):
    if start == end:
        return get_number_of_letters(start)
    res = 0
    for i in range(start, end + 1):
        res += get_number_of_letters(i)
    return res

power_dict = {3: "thousand", 6: "million", 9: "billion"}

word_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
             10: "ten",
             11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
             18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
             70: "seventy",
             80: "eighty", 90: "ninety"}

if __name__ == "__main__":
    print(tests())
    print(get_number_of_letters_range(1, 1000))
