number_length = 1000
i = n = prev_n = 1
while len(str(n)) < number_length:
    n, prev_n = n + prev_n, n
    i += 1
print(i + 1)




