def sum_1_to_n(sum, n):
    if n == 0:
        print(sum)
        return
    sum_1_to_n(sum + n, n - 1)

sum_1_to_n(0, 42)
