def tests():
    test_list = [get_number_of_letters_range(1, 5) == 19,
                 get_number_of_letters_range(342, 342) == 23,
                 get_number_of_letters_range(115, 115) == 20]
    res = all(test_list)
    if not res:
        print(test_list)
    return res


def process_three(number, power):
    # this is the {}, a 3-digit number
    # it is definitely less than a thousand
    # returns the description and units - e.g. thousand, million, billion etc.
    res = 0
    res_string = ""
    hundreds = number // 100 % 10  # e.g. 6 for number 7654
    tens = number // 10 % 10  # e.g 6 for number 4762
    ones = number % 10
    if hundreds:
        phrase = word_dict[hundreds] + "hundred"
        res += len(phrase)
        res_string += phrase
    if hundreds and (tens or ones):
        phrase = "and"
        res += len(phrase)
        res_string += phrase
    if tens == 1:
        phrase = word_dict[tens * 10 + ones]
        res += len(phrase)
        res_string += phrase
    else:
        if tens:
            phrase = word_dict[tens * 10]
            res += len(phrase)
            res_string += phrase
        if ones:
            phrase = word_dict[ones]
            res += len(phrase)
            res_string += phrase
    if power:
        power_data = power_dict[power]
        res += len(power_data)
        res_string += power_data
    return res, res_string


def get_len_and_desc_of_number(number, power):
    # every three digits are processed in exactly the same way
    # {} billion {} million {} thousand {}
    # get the last three digits, get the result
    if number < 1000:
        res = process_three(number % 1000, power)
        return res
    new_smarter = get_len_and_desc_of_number(number // 1000, power + 3)
    last_three = process_three(number % 1000, power)
    res_string = new_smarter[1] + last_three[1]
    return new_smarter[0] + last_three[0], res_string


def get_number_of_letters_range(start, end):
    res = 0
    for i in range(start, end + 1):
        res += get_len_and_desc_of_number(i, 0)[0]
    return res


power_dict = {3: "thousand", 6: "million", 9: "billion"}

word_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
             10: "ten",
             11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
             18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
             70: "seventy",
             80: "eighty", 90: "ninety"}

if __name__ == "__main__":
    print(get_number_of_letters_range(1, 1000))
