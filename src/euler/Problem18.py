from euler.input_Problem18 import input_string_15


def tests():
    global triangle
    triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    return find_max_sum() == 23


def assign_triangle(input_str):
    global triangle
    input_rows = input_str.split("\n")
    triangle = [[int(value) for value in row.split(" ")] for row in input_rows]


def find_max_sum(current_level=0, current_pos=0):
    current_num = triangle[current_level][current_pos]
    if current_level + 1 == len(triangle):
        return max(triangle[current_level][current_pos:current_pos+2])
    left_sum = find_max_sum(current_level+1, current_pos)
    right_sum = find_max_sum(current_level+1, current_pos+1)
    if left_sum > right_sum:
        return current_num + left_sum
    return current_num + right_sum


if __name__ == "__main__":
    print(tests())
    assign_triangle(input_string_15)
    print(find_max_sum())
