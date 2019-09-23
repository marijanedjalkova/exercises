class Node(object):
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        rep = str(self.value)
        if self.next is not None:
            rep += " -> "
            rep += self.next.__str__()
        return rep


def get_sum(node1, node2):
    result = None
    current_result = None
    add_on = 0
    while node1 or node2:
        value1 = node1.value if node1 else 0
        value2 = node2.value if node2 else 0
        sum_digit = value1 + value2 + add_on
        if sum_digit > 9:
            add_on = 1
            sum_digit -= 10
        else:
            add_on = 0
        if not result:
            result = Node(sum_digit)
            current_result = result
        else:
            current_result.next = Node(sum_digit)
            current_result = current_result.next
        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next
    if add_on == 1:
        current_result.next = Node(1)
    return result


if __name__ == "__main__":
    number1 = Node(9)
    number1.next = Node(9)
    number1.next.next = Node(9)
    number2 = Node(1)
    number2.next = Node(0)
    number2.next.next = Node(0)
    global_result = get_sum(number1, number2)
    print("Final result is ", global_result)
