from euler.input_Problem18 import input_string_15
from euler.input_Problem67 import input_string_100
counter = 0
sum_dict = {}


def tests():
    global triangle
    triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    return find_max_sum() == 23


def assign_triangle(input_str):
    global triangle
    input_rows = input_str.split("\n")
    triangle = [[int(value) for value in row.split(" ")] for row in input_rows]


def find_max_sum(current_level=0, current_pos=0):
    global counter
    counter += 1
    current_num = triangle[current_level][current_pos]
    if current_level in sum_dict and current_pos in sum_dict[current_level]:
        return sum_dict[current_level][current_pos]
    if current_level + 1 == len(triangle):
        return max(triangle[current_level][current_pos:current_pos+2])
    left_sum = find_max_sum(current_level+1, current_pos)
    right_sum = find_max_sum(current_level+1, current_pos+1)
    if left_sum > right_sum:
        to_add = left_sum
    else:
        to_add = right_sum
    res = current_num + to_add
    if current_level not in sum_dict:
        sum_dict[current_level] = {}
    sum_dict[current_level][current_pos] = res
    return res


if __name__ == "__main__":
    print(tests())
    assign_triangle(input_string_100)
    counter = 0
    sum_dict.clear()
    if counter == 0 and not sum_dict.keys():
        print("All data clear")
    print(find_max_sum())
    print("Steps made: ", counter)
