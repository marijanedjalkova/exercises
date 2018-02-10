import csv
import string


def tests():
    test1 = (get_alpha_value("COLIN") == 53)
    test2 = (get_order_number("COLIN") == 938)
    test3 = (get_score("COLIN") == 49714)
    test_lst = [test1, test2, test3]
    return all(test_lst)


names = []


def import_names():
    global names
    with open("p022_names.txt", "r") as input_file:
        reader = csv.reader(input_file, delimiter=",")
        for r in reader:
            for name in r:
                names.append(name)
        names = sorted(names)


def get_score(name, order_number=None):
    global names
    if not order_number:
        order_number = get_order_number(name)
    return order_number * get_alpha_value(name)


def get_alpha_value(name):
    res = 0
    for letter in name.lower():
        letter_value = string.ascii_lowercase.index(letter) + 1
        res += letter_value
    return res


def get_order_number(name):
    # basically we shouldn't ever go here
    return names.index(name) + 1


def get_total_score():
    return sum([get_score(name, order_num + 1) for (order_num, name) in enumerate(names)])


if __name__ == "__main__":
    import_names()
    print(tests())
    print(get_total_score())
    # 871198282
