import csv


def import_names():
    with open("p022_names.txt", "r") as input_file:
        reader = csv.reader(input_file, delimiter=",")
        name_lst = []
        for r in reader:
            for name in r:
                name_lst.append(name)
        name_lst = sorted(name_lst)
    return name_lst


if __name__ == "__main__":
    names = import_names()
    print(names[:5])