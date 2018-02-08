def tests():
    global triangle
    triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    return find_max_sum() == 23


input_string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def assign_triangle():
    global triangle
    input_rows = input_string.split("\n")
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
    assign_triangle()
    print(find_max_sum())
