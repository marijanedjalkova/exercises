import time


routes_dict = {}


def add_results(down, right, r, c):
    if r + 1 not in routes_dict:
        routes_dict[r-1] = {}
    routes_dict[r-1][c] = down
    if r not in routes_dict:
        routes_dict[r] = {}
    routes_dict[r][c-1] = right


def get_num_of_routes(r, c):
    if r in routes_dict and c in routes_dict[r]:
        return routes_dict[r][c]
    if 0 in [r, c]:
        return 1
    if r == c == 1:
        return 2
    # sum up results from going down and to the right
    down = get_num_of_routes(r - 1, c)
    right = get_num_of_routes(r, c-1)
    add_results(down, right, r, c)
    return down + right


if __name__ == "__main__":
    start_time = time.time()
    print("Problem 15. Result: ", get_num_of_routes(20, 20))
    print("--- %s seconds ---" % (time.time() - start_time))
